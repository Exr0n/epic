from subprocess import Popen

soup = '''
index.html:smt 2017-03-31
index.html:119 2017-03-30
index.html:118 2017-03-29
index.html:117 2017-03-28
index.html:116 2017-03-27
index.html:115 2017-03-26
index.html:124 2017-04-02
index.html:133 2017-04-09
index.html:142 2017-04-16
index.html:151 2017-04-23
index.html:127 2017-04-05
index.html:136 2017-04-12
index.html:145 2017-04-19
2index.html:130 2017-04-08
index.html:139 2017-04-15
index.html:148 2017-04-22
index.html:157 2017-04-29
index.html:178 2017-05-14
index.html:187 2017-05-21
index.html:196 2017-05-28
index.html:205 2017-06-04
index.html:179 2017-05-15
index.html:180 2017-05-16
index.html:181 2017-05-17
index.html:182 2017-05-18
index.html:183 2017-05-19
index.html:184 2017-05-20
index.html:215 2017-06-12
index.html:216 2017-06-13
index.html:217 2017-06-14
index.html:191 2017-05-25
index.html:200 2017-06-01
index.html:209 2017-06-08

I 2017-07-02
index.html:250 2017-07-09
index.html:259 2017-07-16
index.html:268 2017-07-23
index.html:277 2017-07-30
index.html:260 2017-07-17
index.html:261 2017-07-18
index.html:262 2017-07-19
index.html:263 2017-07-20
index.html:264 2017-07-21
index.html:265 2017-07-22
index.html:256 2017-07-15
index.html:247 2017-07-08
index.html:274 2017-07-29
index.html:283 2017-08-05

C 2017-08-22
index.html:307 2017-08-23
index.html:308 2017-08-24
index.html:313 2017-08-27
index.html:322 2017-09-03
index.html:331 2017-09-10
index.html:340 2017-09-17
index.html:305 2017-08-21
index.html:309 2017-08-25
index.html:319 2017-09-02
index.html:328 2017-09-09
index.html:337 2017-09-16
index.html:346 2017-09-23
'''

dates = []
for line in soup.split('\n'):
    # print(line.split(' '))
    date = line.split(' ')
    if (len(date) > 1):
        dates.append(date[1])

for date in dates:
    print(['git', 'commit', f'--date={date}T00:13:37', '-m', 'epic'])

