from wsgiref.util import FileWrapper
import io
from zipfile import *
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse

from base import mods
from base.models import Auth, Key
import zipfile
from django.http import HttpResponseRedirect



class Question(models.Model):
    desc = models.TextField()

    SCOPES = (
        ('Lit', 'Literature'),
        ('Ent', 'Entertainment'),
        ('Geo', 'Geography'),
        ('His', 'History'),
        ('Sci', 'Science'),
        ('Spo', 'Sports'),
        ('Oth', 'Other'),

    )

    scopes = models.TextField(max_length=14, blank=True, null=True, choices=SCOPES)
    #scopes = models.TextField(blank=True, null=True, choices=SCOPES)

    def __str__(self):
        return self.desc


class QuestionOption(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    number = models.PositiveIntegerField(blank=True, null=True)
    option = models.TextField()

    def save(self):
        if not self.number:
            self.number = self.question.options.count() + 2
        return super().save()

    def __str__(self):
        return '{} ({})'.format(self.option, self.number)


class Voting(models.Model):

    THEMES_VOTATIONS = (
        ('El', 'Electoral'),
        ('Si', 'Self-interest'),
        ('Kw', 'Knowledge'),
        ('Ts', 'Testing'),
        ('Su', 'Survey'),

    )

    TYPES_PREFERENCES = (
        ('H', 'High'),
        ('M', 'Mid'),
        ('L', 'Low'),
    )
    name = models.CharField(max_length=200)
    themeVotation = models.CharField(max_length=14, blank=False, null=False, choices=THEMES_VOTATIONS)
    preference = models.CharField(max_length=14, blank=False, null=False, choices=TYPES_PREFERENCES)
    desc = models.TextField( blank=True, null=True, )
    question = models.ForeignKey(Question, related_name='voting', on_delete=models.CASCADE)

    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    pub_key = models.OneToOneField(Key, related_name='voting', blank=True, null=True, on_delete=models.SET_NULL)
    auths = models.ManyToManyField(Auth, related_name='votings')

    tally = JSONField(blank=True, null=True)
    postproc = JSONField(blank=True, null=True)

    def create_pubkey(self):
        if self.pub_key or not self.auths.count():
            return

        auth = self.auths.first()
        data = {
            "voting": self.id,
            "auths": [ {"name": a.name, "url": a.url} for a in self.auths.all() ],
        }
        key = mods.post('mixnet', baseurl=auth.url, json=data)
        pk = Key(p=key["p"], g=key["g"], y=key["y"])
        pk.save()
        self.pub_key = pk
        self.save()

    def get_votes(self, token=''):
        # gettings votes from store
        votes = mods.get('store', params={'voting_id': self.id}, HTTP_AUTHORIZATION='Token ' + token)
        # anon votes
        return [[i['a'], i['b']] for i in votes]

    def tally_votes(self, token=''):
        '''
        The tally is a shuffle and then a decrypt
        '''

        votes = self.get_votes(token)

        auth = self.auths.first()
        shuffle_url = "/shuffle/{}/".format(self.id)
        decrypt_url = "/decrypt/{}/".format(self.id)
        auths = [{"name": a.name, "url": a.url} for a in self.auths.all()]

        # first, we do the shuffle
        data = { "msgs": votes }
        response = mods.post('mixnet', entry_point=shuffle_url, baseurl=auth.url, json=data,
                response=True)
        if response.status_code != 200:
            # TODO: manage error
            pass

        # then, we can decrypt that
        data = {"msgs": response.json()}
        response = mods.post('mixnet', entry_point=decrypt_url, baseurl=auth.url, json=data,
                response=True)

        if response.status_code != 200:
            # TODO: manage error
            pass

        self.tally = response.json()
        self.save()

        self.do_postproc()

    def do_postproc(self):
        tally = self.tally
        options = self.question.options.all()

        opts = []
        for opt in options:
            if isinstance(tally, list):
                votes = tally.count(opt.number)
            else:
                votes = 0
            opts.append({
                'option': opt.option,
                'number': opt.number,
                'votes': votes
            })

        data = { 'type': 'IDENTITY', 'options': opts }
        postp = mods.post('postproc', json=data)

        self.postproc = postp
        self.save()

    def tally_to_file(self, token=''):

        id = self.id
        name = self.name
        desc = self.desc
        start_date = self.start_date
        end_date = self.end_date
        question = self.question

        postproc_list = self.postproc

        doc_name = './voting/static_files/tally_report_' + str(id) + '.txt'
        zip_name = './voting/static_files/tally_report_' + str(id) + '.zip'

        document = 'Id Voting: ' + str(id) + '\n' +'Name: ' + str(name) + '\n' + 'Description: ' + str(desc) + '\n' + 'Start Date: ' + str(
            start_date) + '\n' + 'End Date: ' + str(end_date) + '\n'+'Question: ' + str(question) + '\n' + 'Options: ' + '\n'

        if(postproc_list!=None):
            for postproc in postproc_list:
                document = document + 'Option '+str(postproc['number'])+': '+str(
                    postproc['option']) + ' - Votes: ' + str(postproc['votes']) + '\n'

        print("LOG: Save Tally in File")

        f = open(doc_name, 'w')
        try:
            f.write(document)
        finally:
            f.close()

        doc_zip = zipfile.ZipFile(zip_name, 'w')
        doc_zip.write(doc_name, compress_type=zipfile.ZIP_DEFLATED)

        doc_zip.close()

    def __str__(self):
        return self.name

