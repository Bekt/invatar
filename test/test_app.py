# -*- coding: utf-8 -*-
from invatar import app


class TestOptions(object):

    def assert_upper(self, text, res):
        assert res == text.upper()

    def test_upper(self):
        opt = app._build_options(u'a', {})
        self.assert_upper(u'a', opt['text'])

        opt = app._build_options(u'kb', {})
        self.assert_upper(u'kb', opt['text'])

    def test_upper_cyrillic(self):
        opt = app._build_options(u'фп', {})
        self.assert_upper(u'фп', opt['text'])
