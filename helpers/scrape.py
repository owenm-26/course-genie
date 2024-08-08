import requests
import json

def fetch_and_write_response():

    cookies = {
        'apt.uid': 'AP-PQQY5YJEHTTA-2-1662408018703-16633267.0.2.02894642-1485-4669-9d4f-fb2d9ac278f1',
        '_ga_8VKDDK19RX': 'GS1.1.1693935861.2.0.1693935864.0.0.0',
        '_ga_J8M8M8YDL8': 'GS1.1.1704844486.2.0.1704844490.0.0.0',
        'uiscgi_prod': '427c734f609c57efbdac6e2cbfd750fd:prod',
        '__utmc': '21468840',
        '_ga_Y5R6LRBR62': 'GS1.1.1708316690.1.1.1708316702.0.0.0',
        'PS_TokenSite': 'https://mybustudent.bu.edu/psp/BUPRD/?JSESSIONID',
        'SignOnDefault': '',
        'hpt_institution': 'BU001',
        '_ce.irv': 'new',
        'cebs': '1',
        'cebsp_': '1',
        '_ga_E89JCFZ56Z': 'GS1.1.1712078098.1.1.1712078234.0.0.0',
        '_ce.s': 'v~d8bc055f2ac3c3f6649b65803faf40c5b628305a~lcw~1712078234106~lva~1712078098938~vpv~0~v11.fhb~1712078099087~v11.lhb~1712078220161~v11.cs~431848~v11.s~88be8010-f114-11ee-8131-2fcade643d63~v11.sla~1712078234124~v11.send~1712078234106~lcw~1712078234125',
        '_ga_XSV7DMEHRQ': 'GS1.1.1712079029.1.1.1712079078.0.0.0',
        '_ga_325610863': 'GS1.1.1712079029.1.0.1712079078.0.0.0',
        '_ga_7J2VGRSJEX': 'GS1.1.1712936663.5.0.1712936663.0.0.0',
        '_ga_2V6PP6D2G4': 'GS1.1.1713187521.3.1.1713187683.0.0.0',
        '_ga_RM036L5NFX': 'GS1.1.1713377968.2.1.1713378101.0.0.0',
        '_ga_6209C9CMNX': 'GS1.1.1713377968.1.1.1713378101.0.0.0',
        'lcsrftoken': 'M/UxMQm/0dS4AkkBv23Z7gQcbetmOaGQu7A0fdr8lVA=',
        '_opensaml_req_ss%3Amem%3Aa74aa525a1ba5b9831c7f69013113a7e24adb28cffca37b2f768d078970379f5': '_413525007373cd3e7b794ed6616759e2',
        '_opensaml_req_ss%3Amem%3Abd0bd1ba3af62e060ab9d943866cce747f245d122f485e519258ef893cf72406': '_2687610d1e0c7be30327ac444251c008',
        '_clck': '17wx2ql%7C2%7Cfl7%7C0%7C1365',
        '_ga_6VXTC1Y945': 'GS1.1.1713923996.3.1.1713924155.0.0.0',
        '_ga_PMCMRTPJSG': 'GS1.1.1713923997.3.1.1713924155.0.0.0',
        '_ga_NR29RQ32SV': 'GS1.1.1714421459.1.0.1714421463.0.0.0',
        '_ga_6DQRRMGKFJ': 'GS1.1.1714587083.1.1.1714587184.0.0.0',
        'AMP_075dfa7287': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI1NmE4MTA4OS1kY2VlLTRmMjItODI2My0xZGQwZDRmYTE2YjAlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzE1MDA0OTg0NDIwJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcxNTAwNTEwNDMwMSU3RA==',
        '_ga_C314QG7LHT': 'GS1.1.1715005123.10.1.1715005645.0.0.1579552093',
        '_ga_L4SD8HKLDR': 'GS1.1.1715445670.20.1.1715445692.0.0.0',
        '_opensaml_req_ss%3Amem%3A708e66f12cc869fe37826b44ff03ff5952923315ed7653ecdef7cf1e04d09c61': '_47e0d12b5966ab3832b4df0eb6f533cf',
        '_opensaml_req_ss%3Amem%3A7ae3c65ae0e2457982bf8c80255a64232cda6611c8d351423da058aaa277118b': '_a306efa934db83c1913b62184fcbda61',
        '_opensaml_req_ss%3Amem%3Aa829e76517274bca9574b61f126e4e28879d41a98a74a0e1fa0a0ab8f935a0a1': '_d8e65917a676b8c9850ba389ab7573f3',
        '_opensaml_req_ss%3Amem%3A8c544bd76fdd360062dc8a6ff523abc43d6ba5d304426a70f7068242429c4656': '_9da6fa980d47b121a249ceef1165d412',
        '_ga_RNH3YRWTR0': 'GS1.1.1719862953.4.0.1719862959.0.0.0',
        '_gcl_au': '1.1.806474157.1720100717',
        '_fbp': 'fb.1.1720100717481.66506904913585472',
        '_ga_LFYP5W9TKM': 'GS1.1.1720103912.3.0.1720103912.0.0.0',
        '_opensaml_req_ss%3Amem%3A253ca2465e6cee3c5b23bbae7b17ec4b8ffe2ad4bbc2a8c84fb4989f6a311945': '_ff477abb93b0f7620a7870c3a50a323c',
        '_ga_WQG2H3DG4P': 'GS1.1.1720466298.7.1.1720468159.0.0.0',
        '_opensaml_req_ss%3Amem%3A34fc9777137eb227b9b247b92dd2faaa68a31a8f2f5d1cc3c332eb15d1a6c8b0': '_f87319ac1ccc60587ccf937b6d1b3662',
        '_opensaml_req_ss%3Amem%3A726a7afc1682949b4b38ef82d90aa7b904942b52411a64566dce8549a4c0beb7': '_7f303cd5cb34abaea2c4ea3b80d30611',
        '_opensaml_req_ss%3Amem%3Afb376c89426535eefc760cc0bfabd5cbed80138ce1e6b703c35acf971b6cea2b': '_f8a0a6d02ad566a76115b46a9cbcc13b',
        '_opensaml_req_ss%3Amem%3Adc78b185698746391c9b244001b0c317181c4b6b1b6b8c69e14e400f368538f4': '_f20a25ef93d3445dc0a6676ba372a7a3',
        '_opensaml_req_ss%3Amem%3A2e15994c70d181f6b41f5e2a7a6ad626904a2e275f943e711c5113f51f45e5b6': '_7f1f861eccf40b59af201b67a93e00b9',
        '_opensaml_req_ss%3Amem%3A9ceea617cc4ff551d8294ff15f2d155c91d934e84c9b4805a110916854a09ba4': '_2ff7eec0c047ec32a1933a8b2217b76f',
        '_opensaml_req_ss%3Amem%3A9f6fb2b22b4e1fa681ed1bff341c1d1269c26b6776ee26c7df455aa70180f772': '_c72f0b42026ed5c1c8182a0d8e1c3187',
        '_opensaml_req_ss%3Amem%3Ad783fb4640b10a2ffa08c55cc24f13f48070d821574b5d259e39ef2a5cc0e950': '_6c307869351d28bb74e83e858f6d1ea6',
        '_ga_0P3BDYKVG0': 'GS1.1.1722118225.6.0.1722119937.0.0.0',
        '_ga_VY3HKSHTD3': 'GS1.1.1722277276.4.0.1722277276.0.0.0',
        '_uetvid': '88a38c30f11411eeaa8a61046c1da480',
        '_ga_4M6L78NGBY': 'GS1.1.1722466543.1.0.1722466552.51.0.2093736198',
        '_ga_B51FJB0BGL': 'GS1.2.1722466579.2.0.1722466579.0.0.0',
        '_ga_X00M2PB2HY': 'GS1.1.1722466543.24.1.1722466963.0.0.0',
        '_ga_E08X766WBX': 'GS1.2.1722467810.2.0.1722467810.0.0.0',
        '_ga_B7YV5R0XM7': 'GS1.1.1722467838.1.0.1722467843.0.0.0',
        '__utma': '21468840.1613972037.1711942563.1722466589.1722467912.18',
        '__utmz': '21468840.1722467912.18.12.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
        '_ga_HVBYYX9KF6': 'GS1.1.1722467912.6.0.1722467919.0.0.0',
        '_ga': 'GA1.1.1613972037.1711942563',
        '_opensaml_req_ss%3Amem%3Af8ea508e7a973112bdcc3e5ced653b4c2165444b34de14dc1abdf4e6a3c92543': '_a4a7fb495b736d52f316a7393555d76c',
        '_opensaml_req_ss%3Amem%3Ad8aba495a54e427b641c0ad3b182c4a0980dc084bbca4d33a44c3a88cbddc9aa': '_861a4b2176078e4fd3ee2a1c7636c76d',
        '_opensaml_req_ss%3Amem%3Aa5bfa57f8864f5046a3c939fd96884587e84d48518d04684e2477310725dc248': '_a4446c459e9bbcaccb54fb4d80ed9fd7',
        'mybustudent-PORTAL-PSJSESSIONID': 'c42557e68f5924d37d8f0a8d8028df6ab07186cb',
        '_opensaml_req_ss%3Amem%3Ae215b423a7b7e1f395a1e77ad006763ce4c01824d3fd9b883c15d4109dfa0155': '_cf97114a1f8ee3d944cd83ee747df953',
        '_ga_0Z1EBE5RV7': 'GS1.1.1723071166.65.0.1723071166.0.0.0',
        '_ga_8CFVMTVJ2Q': 'GS1.1.1723071167.1.0.1723071167.0.0.0',
        'PS_LASTSITE': 'https://mybustudent.bu.edu/psp/BUPRD/',
        'ExpirePage': 'https://mybustudent.bu.edu/psp/BUPRD/',
        'PS_LOGINLIST': 'https://mybustudent.bu.edu/BUPRD',
        'ps_theme': 'node:SA portal:EMPLOYEE theme_id:BU_THEME_FLUID css:BU_THEME_FLUID_859 css_f:BU_GLOBAL_OVERRIDE_FL accessibility:N macroset:BU_DEFAULT_MACROSET_859 formfactor:3 piamode:2',
        'PS_DEVICEFEATURES': 'width:1280 height:832 pixelratio:1.5 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0 maf:0',
        '_shibsession_64656661756c7468747470733a2f2f6d79627573747564656e742e62752e6564752f73702f73686962626f6c657468': '_4426a26023d09d0921f94e1066221fea',
        'JSESSIONID': '3QIzh4MXTkJFysGciFEJ4WG_oIvKadqA!-2028705533',
        'PS_TOKEN': 'pAAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4AcQg4AC4AMQAwABT+3D2WzrztCyUHKR10QHGIHaCPW2QAAAAFAFNkYXRhWHicPYpLDkBAEAVrEEtxEcIQGUsRxMIn2DuD+zmcx0J3uuql8y4g8D1j5Nvjm3hhomFjFGcx7KSBaGWn5+CkVSotGZaSRHY/c22qb/WxEGu1nNJ7PLCkDAw=',
        'https%3a%2f%2fmybustudent.bu.edu%2fpsp%2fbuprd%2femployee%2fsa%2frefresh': 'list: %3ftab%3ddefault|%3frp%3ddefault|%3ftab%3dhpt_student_general_tab|%3frp%3dhpt_student_general_tab|%3ftab%3dhpt_student_academics_tab|%3frp%3dhpt_student_academics_tab|%3ftab%3dhpt_student_financials_tab|%3frp%3dhpt_student_financials_tab|%3ftab%3dremoteunifieddashboard|%3frp%3dremoteunifieddashboard',
        '_ga_F7T3KG2073': 'GS1.1.1723146400.69.1.1723146405.0.0.0',
        'CSRFCookie': '932060bb-845a-4720-8a34-13faedcca91b',
        'PS_TOKENEXPIRE': '8_Aug_2024_19:46:54_GMT',
    }

    headers = {
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': 'apt.uid=AP-PQQY5YJEHTTA-2-1662408018703-16633267.0.2.02894642-1485-4669-9d4f-fb2d9ac278f1; _ga_8VKDDK19RX=GS1.1.1693935861.2.0.1693935864.0.0.0; _ga_J8M8M8YDL8=GS1.1.1704844486.2.0.1704844490.0.0.0; uiscgi_prod=427c734f609c57efbdac6e2cbfd750fd:prod; __utmc=21468840; _ga_Y5R6LRBR62=GS1.1.1708316690.1.1.1708316702.0.0.0; PS_TokenSite=https://mybustudent.bu.edu/psp/BUPRD/?JSESSIONID; SignOnDefault=; hpt_institution=BU001; _ce.irv=new; cebs=1; cebsp_=1; _ga_E89JCFZ56Z=GS1.1.1712078098.1.1.1712078234.0.0.0; _ce.s=v~d8bc055f2ac3c3f6649b65803faf40c5b628305a~lcw~1712078234106~lva~1712078098938~vpv~0~v11.fhb~1712078099087~v11.lhb~1712078220161~v11.cs~431848~v11.s~88be8010-f114-11ee-8131-2fcade643d63~v11.sla~1712078234124~v11.send~1712078234106~lcw~1712078234125; _ga_XSV7DMEHRQ=GS1.1.1712079029.1.1.1712079078.0.0.0; _ga_325610863=GS1.1.1712079029.1.0.1712079078.0.0.0; _ga_7J2VGRSJEX=GS1.1.1712936663.5.0.1712936663.0.0.0; _ga_2V6PP6D2G4=GS1.1.1713187521.3.1.1713187683.0.0.0; _ga_RM036L5NFX=GS1.1.1713377968.2.1.1713378101.0.0.0; _ga_6209C9CMNX=GS1.1.1713377968.1.1.1713378101.0.0.0; lcsrftoken=M/UxMQm/0dS4AkkBv23Z7gQcbetmOaGQu7A0fdr8lVA=; _opensaml_req_ss%3Amem%3Aa74aa525a1ba5b9831c7f69013113a7e24adb28cffca37b2f768d078970379f5=_413525007373cd3e7b794ed6616759e2; _opensaml_req_ss%3Amem%3Abd0bd1ba3af62e060ab9d943866cce747f245d122f485e519258ef893cf72406=_2687610d1e0c7be30327ac444251c008; _clck=17wx2ql%7C2%7Cfl7%7C0%7C1365; _ga_6VXTC1Y945=GS1.1.1713923996.3.1.1713924155.0.0.0; _ga_PMCMRTPJSG=GS1.1.1713923997.3.1.1713924155.0.0.0; _ga_NR29RQ32SV=GS1.1.1714421459.1.0.1714421463.0.0.0; _ga_6DQRRMGKFJ=GS1.1.1714587083.1.1.1714587184.0.0.0; AMP_075dfa7287=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI1NmE4MTA4OS1kY2VlLTRmMjItODI2My0xZGQwZDRmYTE2YjAlMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzE1MDA0OTg0NDIwJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTcxNTAwNTEwNDMwMSU3RA==; _ga_C314QG7LHT=GS1.1.1715005123.10.1.1715005645.0.0.1579552093; _ga_L4SD8HKLDR=GS1.1.1715445670.20.1.1715445692.0.0.0; _opensaml_req_ss%3Amem%3A708e66f12cc869fe37826b44ff03ff5952923315ed7653ecdef7cf1e04d09c61=_47e0d12b5966ab3832b4df0eb6f533cf; _opensaml_req_ss%3Amem%3A7ae3c65ae0e2457982bf8c80255a64232cda6611c8d351423da058aaa277118b=_a306efa934db83c1913b62184fcbda61; _opensaml_req_ss%3Amem%3Aa829e76517274bca9574b61f126e4e28879d41a98a74a0e1fa0a0ab8f935a0a1=_d8e65917a676b8c9850ba389ab7573f3; _opensaml_req_ss%3Amem%3A8c544bd76fdd360062dc8a6ff523abc43d6ba5d304426a70f7068242429c4656=_9da6fa980d47b121a249ceef1165d412; _ga_RNH3YRWTR0=GS1.1.1719862953.4.0.1719862959.0.0.0; _gcl_au=1.1.806474157.1720100717; _fbp=fb.1.1720100717481.66506904913585472; _ga_LFYP5W9TKM=GS1.1.1720103912.3.0.1720103912.0.0.0; _opensaml_req_ss%3Amem%3A253ca2465e6cee3c5b23bbae7b17ec4b8ffe2ad4bbc2a8c84fb4989f6a311945=_ff477abb93b0f7620a7870c3a50a323c; _ga_WQG2H3DG4P=GS1.1.1720466298.7.1.1720468159.0.0.0; _opensaml_req_ss%3Amem%3A34fc9777137eb227b9b247b92dd2faaa68a31a8f2f5d1cc3c332eb15d1a6c8b0=_f87319ac1ccc60587ccf937b6d1b3662; _opensaml_req_ss%3Amem%3A726a7afc1682949b4b38ef82d90aa7b904942b52411a64566dce8549a4c0beb7=_7f303cd5cb34abaea2c4ea3b80d30611; _opensaml_req_ss%3Amem%3Afb376c89426535eefc760cc0bfabd5cbed80138ce1e6b703c35acf971b6cea2b=_f8a0a6d02ad566a76115b46a9cbcc13b; _opensaml_req_ss%3Amem%3Adc78b185698746391c9b244001b0c317181c4b6b1b6b8c69e14e400f368538f4=_f20a25ef93d3445dc0a6676ba372a7a3; _opensaml_req_ss%3Amem%3A2e15994c70d181f6b41f5e2a7a6ad626904a2e275f943e711c5113f51f45e5b6=_7f1f861eccf40b59af201b67a93e00b9; _opensaml_req_ss%3Amem%3A9ceea617cc4ff551d8294ff15f2d155c91d934e84c9b4805a110916854a09ba4=_2ff7eec0c047ec32a1933a8b2217b76f; _opensaml_req_ss%3Amem%3A9f6fb2b22b4e1fa681ed1bff341c1d1269c26b6776ee26c7df455aa70180f772=_c72f0b42026ed5c1c8182a0d8e1c3187; _opensaml_req_ss%3Amem%3Ad783fb4640b10a2ffa08c55cc24f13f48070d821574b5d259e39ef2a5cc0e950=_6c307869351d28bb74e83e858f6d1ea6; _ga_0P3BDYKVG0=GS1.1.1722118225.6.0.1722119937.0.0.0; _ga_VY3HKSHTD3=GS1.1.1722277276.4.0.1722277276.0.0.0; _uetvid=88a38c30f11411eeaa8a61046c1da480; _ga_4M6L78NGBY=GS1.1.1722466543.1.0.1722466552.51.0.2093736198; _ga_B51FJB0BGL=GS1.2.1722466579.2.0.1722466579.0.0.0; _ga_X00M2PB2HY=GS1.1.1722466543.24.1.1722466963.0.0.0; _ga_E08X766WBX=GS1.2.1722467810.2.0.1722467810.0.0.0; _ga_B7YV5R0XM7=GS1.1.1722467838.1.0.1722467843.0.0.0; __utma=21468840.1613972037.1711942563.1722466589.1722467912.18; __utmz=21468840.1722467912.18.12.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _ga_HVBYYX9KF6=GS1.1.1722467912.6.0.1722467919.0.0.0; _ga=GA1.1.1613972037.1711942563; _opensaml_req_ss%3Amem%3Af8ea508e7a973112bdcc3e5ced653b4c2165444b34de14dc1abdf4e6a3c92543=_a4a7fb495b736d52f316a7393555d76c; _opensaml_req_ss%3Amem%3Ad8aba495a54e427b641c0ad3b182c4a0980dc084bbca4d33a44c3a88cbddc9aa=_861a4b2176078e4fd3ee2a1c7636c76d; _opensaml_req_ss%3Amem%3Aa5bfa57f8864f5046a3c939fd96884587e84d48518d04684e2477310725dc248=_a4446c459e9bbcaccb54fb4d80ed9fd7; mybustudent-PORTAL-PSJSESSIONID=c42557e68f5924d37d8f0a8d8028df6ab07186cb; _opensaml_req_ss%3Amem%3Ae215b423a7b7e1f395a1e77ad006763ce4c01824d3fd9b883c15d4109dfa0155=_cf97114a1f8ee3d944cd83ee747df953; _ga_0Z1EBE5RV7=GS1.1.1723071166.65.0.1723071166.0.0.0; _ga_8CFVMTVJ2Q=GS1.1.1723071167.1.0.1723071167.0.0.0; PS_LASTSITE=https://mybustudent.bu.edu/psp/BUPRD/; ExpirePage=https://mybustudent.bu.edu/psp/BUPRD/; PS_LOGINLIST=https://mybustudent.bu.edu/BUPRD; ps_theme=node:SA portal:EMPLOYEE theme_id:BU_THEME_FLUID css:BU_THEME_FLUID_859 css_f:BU_GLOBAL_OVERRIDE_FL accessibility:N macroset:BU_DEFAULT_MACROSET_859 formfactor:3 piamode:2; PS_DEVICEFEATURES=width:1280 height:832 pixelratio:1.5 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0 maf:0; _shibsession_64656661756c7468747470733a2f2f6d79627573747564656e742e62752e6564752f73702f73686962626f6c657468=_4426a26023d09d0921f94e1066221fea; JSESSIONID=3QIzh4MXTkJFysGciFEJ4WG_oIvKadqA!-2028705533; PS_TOKEN=pAAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4AcQg4AC4AMQAwABT+3D2WzrztCyUHKR10QHGIHaCPW2QAAAAFAFNkYXRhWHicPYpLDkBAEAVrEEtxEcIQGUsRxMIn2DuD+zmcx0J3uuql8y4g8D1j5Nvjm3hhomFjFGcx7KSBaGWn5+CkVSotGZaSRHY/c22qb/WxEGu1nNJ7PLCkDAw=; https%3a%2f%2fmybustudent.bu.edu%2fpsp%2fbuprd%2femployee%2fsa%2frefresh=list: %3ftab%3ddefault|%3frp%3ddefault|%3ftab%3dhpt_student_general_tab|%3frp%3dhpt_student_general_tab|%3ftab%3dhpt_student_academics_tab|%3frp%3dhpt_student_academics_tab|%3ftab%3dhpt_student_financials_tab|%3frp%3dhpt_student_financials_tab|%3ftab%3dremoteunifieddashboard|%3frp%3dremoteunifieddashboard; _ga_F7T3KG2073=GS1.1.1723146400.69.1.1723146405.0.0.0; CSRFCookie=932060bb-845a-4720-8a34-13faedcca91b; PS_TOKENEXPIRE=8_Aug_2024_19:46:54_GMT',
        'Referer': 'https://mybustudent.bu.edu/psc/BUPRD/EMPLOYEE/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_Main?acad_group=BU1&enrl_stat=O&crse_attr=HUB',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
        'accept': 'application/json',
        'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    params = {
        'institution': 'BU001',
        'term': '2248',
        'date_from': '',
        'date_thru': '',
        'subject': '',
        'subject_like': '',
        'catalog_nbr': '',
        'start_time_equals': '',
        'start_time_ge': '',
        'end_time_equals': '',
        'end_time_le': '',
        'days': '',
        'campus': '',
        'location': '',
        'x_acad_career': '',
        'acad_group': 'BU1',
        'rqmnt_designtn': '',
        'instruction_mode': '',
        'keyword': '',
        'class_nbr': '',
        'acad_org': '',
        'enrl_stat': 'O',
        'crse_attr': 'HUB',
        'crse_attr_value': '',
        'instructor_name': '',
        'instr_first_name': '',
        'session_code': '',
        'units': '',
        'trigger_search': '',
        'page': '1',
    }

    response = requests.get(
        'https://mybustudent.bu.edu/psc/BUPRD/EMPLOYEE/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_ClassSearch',
        params=params,
        cookies=cookies,
        headers=headers,
    )



    # will need to fix this issue later but if get this then you need to remake the cURL -> request thing 
    if(response.content.startswith(b'<!DOCTYPE html>\r\n<html')):
        print('FAILED, please log in')
        return ({"status": 405, "body": 'FAILED, please log in'})
    
    with open('open_courses.txt', 'wb') as file:
        file.write(response.content)
    
    json_str = response.content.decode('utf-8')
    data = json.loads(json_str) 
    return ({"status": response.status_code, "body":data})

fetch_and_write_response()