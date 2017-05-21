# -*- coding: UTF-8 -*-
import codecs
import time
date = time.strftime("%Y-%m-%d", time.localtime())
days = time.strftime("%j", time.localtime())
count = int(days) - 15
filename = date + "-soyaine-daily-" + str(count) + ".md"
with codecs.open( filename , "w", encoding="utf-8" ) as f :
         f.write("---\nlayout: post\ntitle: \"所丫日报\" \ndate: " + date + " \ncategory: soyainedaily \nexcerpt: \"\"\n---")
