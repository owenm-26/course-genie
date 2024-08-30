import requests
import json

# you will need to update these cookies/params/etc. regularly
def fetch_and_write_response():
    cookies = {
        'SignOnDefault': '',
        'hpt_institution': 'BU001',
        '_opensaml_req_ss%3Amem%3Aca4e651a2dac6323407e6c8e6a1969db70691ec48571d95261acdd8aee982719': '_638298e804531e6f6d31bf94fc9d16f6',
        'uiscgi_prod': 'a8511dcdb8f7945cd1f4310cbde1d614:prod',
        '_ga_8CFVMTVJ2Q': 'GS1.1.1723071785.1.1.1723071849.0.0.0',
        '_opensaml_req_ss%3Amem%3Add2c81b400cea1b2c09b33b0df810367da19c83a0903252e9e3203b82f94e1ab': '_e8323b5504681fe6e2ecc05df9a68efe',
        '__utmc': '21468840',
        '_gac_UA-45347247-2': '1.1723214024.Cj0KCQjwn7mwBhCiARIsAGoxjaJQ5KkqfCfc-_3e8nbBlAq3sGy07slqeZOgMHTagyoLcV8LOmvda7EaAqY9EALw_wcB',
        '_gcl_aw': 'GCL.1723214024.Cj0KCQjwn7mwBhCiARIsAGoxjaJQ5KkqfCfc-_3e8nbBlAq3sGy07slqeZOgMHTagyoLcV8LOmvda7EaAqY9EALw_wcB',
        '_gcl_dc': 'GCL.1723214024.Cj0KCQjwn7mwBhCiARIsAGoxjaJQ5KkqfCfc-_3e8nbBlAq3sGy07slqeZOgMHTagyoLcV8LOmvda7EaAqY9EALw_wcB',
        '_gcl_gs': '2.1.k1$i1723214021',
        '_ga_QHQ86LM5JZ': 'GS1.1.1723214024.1.1.1723214469.57.0.0',
        '_opensaml_req_ss%3Amem%3A6c54fe4550ff1f34247373850f02ecd72c7a7eab2f0169de67a9c66b8a7a5cf5': '_2998b2a931067deaca4aedb1061fa281',
        '_opensaml_req_ss%3Amem%3A030c25fba1fee8380a95ff626b4a657d921897abb862593d143f76deed5e8dd0': '_226c712e82675b73c7a4bbba43e17061',
        '_opensaml_req_ss%3Amem%3A846b8a7ae7752451eeb890a0c7d045d78131c739d1131fa0afab88d753f97bf7': '_2861a9565a48abe6de58fe2ee051747b',
        '_opensaml_req_ss%3Amem%3A875184bd6382b7a0618ce22c8ce3517d82dfb244ed8aff43d841ecf7b3f913f4': '_196fe17180b238ddb9eb0c5c891c155f',
        '_opensaml_req_ss%3Amem%3A54f1d3a06d8caedf420d18416724b07c3d01a6fbdd2230f1ea9c0cae2f0f2c99': '_dbd280cbb14d70da0738dfda992ae112',
        '_opensaml_req_ss%3Amem%3A3bb288a870e610700c7457801c2bd5018314fd0f3758b16a6057b37ae98e2104': '_4ad4442e8592272e294c9c721bd109e1',
        '_opensaml_req_ss%3Amem%3Af405b37ade3d8a99464cda1f246e32f87522c42b9567181c2dfdb65510ec4e60': '_90ed58de656bd0758a060fc9b2983e7e',
        '_opensaml_req_ss%3Amem%3A022b28964d940122405fc1741cf1a9acb4f408b86f7fcb43b53b3d614fa586ae': '_e1751e0715ea9c807535f6133fea746d',
        '_opensaml_req_ss%3Amem%3A97eff7ff4fd4ab9e83efbcf451f5a5d05bd7dad4df7dfb5605b1d2f0f2233f08': '_8792ce7abc97695443c12d36093cbeb3',
        '_opensaml_req_ss%3Amem%3A3541c826ee3ceaee65b0e06b65e1b09638e2f1ae8bf036a0a64b2c2c415e957f': '_75f799f8ffdecb6cd74071fdb39a50f4',
        '_opensaml_req_ss%3Amem%3Adabdab0cbca6f878079b99196752b07c5966918af1be0dcac1c48d6deac8cbfd': '_409792138bdf35b585771268b75dab35',
        'mybustudent-PORTAL-PSJSESSIONID': '461be682d445cfd26ee479733657ebe2f30ee9e0',
        '_opensaml_req_ss%3Amem%3Af38bd2447cbb9295603dec9578d1ae58a87473e4bd58fc6f3b9c5a90c944c31b': '_395af84d49163f24a86c8f4c3b2a9e93',
        'PS_LASTSITE': 'https://mybustudent.bu.edu/psp/BUPRD/',
        'ExpirePage': 'https://mybustudent.bu.edu/psp/BUPRD/',
        'PS_TokenSite': 'https://mybustudent.bu.edu/psp/BUPRD/?JSESSIONID',
        'PS_LOGINLIST': 'https://mybustudent.bu.edu/BUPRD',
        'ps_theme': 'node:SA portal:EMPLOYEE theme_id:BU_THEME_FLUID css:BU_THEME_FLUID_859 css_f:BU_GLOBAL_OVERRIDE_FL accessibility:N macroset:BU_DEFAULT_MACROSET_859 formfactor:3 piamode:2',
        'PS_DEVICEFEATURES': 'width:1440 height:900 pixelratio:2 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0 maf:0',
        '_ga_V91YQBS3LZ': 'GS1.1.1723831762.1.0.1723831838.0.0.0',
        '_gcl_au': '1.1.543065038.1723832235',
        '_scid': '35860a37-c3ca-44b6-b983-26bb54813388',
        '_scid_r': '35860a37-c3ca-44b6-b983-26bb54813388',
        '_hjSessionUser_1849442': 'eyJpZCI6IjUxNjRmMjQyLWNlYzYtNTk2Ny05NmY0LTU4MzMwN2EzYzZmNyIsImNyZWF0ZWQiOjE3MjM4MzIyMzU5NzAsImV4aXN0aW5nIjp0cnVlfQ==',
        '_fbp': 'fb.1.1723832236148.376725651588950729',
        '_sctr': '1%7C1723780800000',
        '_ga_JGVBW8B4Z9': 'GS1.1.1723845318.2.0.1723845318.60.0.0',
        '_ga_E08X766WBX': 'GS1.2.1724189740.1.0.1724189740.0.0.0',
        'PS_TokenSite': 'https://public.mybustudent.bu.edu/psp/BUPRD/?public-PORTAL-PSJSESSIONID',
        '_ga_NC4W1T8DC6': 'GS1.1.1724190127.1.1.1724190221.0.0.0',
        '_ga_HVBYYX9KF6': 'GS1.1.1724198276.7.0.1724198276.0.0.0',
        '_clck': '1raffei%7C2%7Cfok%7C0%7C1696',
        '_ga_PMCMRTPJSG': 'GS1.1.1724376383.1.1.1724376461.0.0.0',
        '_ga_6VXTC1Y945': 'GS1.1.1724376382.1.1.1724376473.0.0.0',
        '_ga_2V6PP6D2G4': 'GS1.1.1724710679.2.0.1724710679.0.0.0',
        '__utma': '21468840.1344430284.1722957096.1724190252.1724788829.6',
        '__utmz': '21468840.1724788829.6.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)',
        '_ga_0Z1EBE5RV7': 'GS1.1.1724788828.13.1.1724788871.0.0.0',
        '_ga_WQG2H3DG4P': 'GS1.1.1724788829.1.1.1724788871.0.0.0',
        '_opensaml_req_ss%3Amem%3A4e64223f5c6639edf0643f00ed7ae341c2a641a2ddf837bab5393c732c6c6a45': '_9db25e03669015e4789702c85da060cf',
        '_opensaml_req_ss%3Amem%3A36c837dcc9c004bdfdddb243afea056d392e411fd8a8122a62a2dce9f3a0b370': '_de0144681571565e8dd067d0b2bf1208',
        '_opensaml_req_ss%3Amem%3A9129019dc585039f276268cce34cc46167bbda27ac05a886f17180d8d6c648b5': '_a4f851e7e947e7ee497f3697e4f2bdf3',
        '_gid': 'GA1.2.1132378177.1724971981',
        '_ga': 'GA1.1.1344430284.1722957096',
        '_ga_L4SD8HKLDR': 'GS1.1.1724979673.3.0.1724979673.0.0.0',
        'https%3a%2f%2fpublic.mybustudent.bu.edu%2fpsp%2fbuprd%2femployee%2fsa%2frefresh': 'list: %3ftab%3ddefault|%3frp%3ddefault|%3ftab%3dremoteunifieddashboard|%3frp%3dremoteunifieddashboard',
        'nullemployee%2fsa%2frefresh': 'list: %3ftab%3drefresh_all_tabs',
        'hpt_institution': 'BU001',
        'CSRFCookie': 'f7d2e3ff-61a3-41aa-99a3-687c1889798c',
        'public-PORTAL-PSJSESSIONID': 'XEmg4b7ZxhLqI9UDJhO_J8zkOc1Y8Gsg!1579944880',
        'X-Oracle-BMC-LBS-Route': '75f54d5ae18383bd0d20b006de3a209f3f6223e1e75e63566915a64c6ac704bcdc340990d42672cad21159007a251d416faef3cc67fe8210a8c699da',
        '_ga_F7T3KG2073': 'GS1.1.1724981092.17.1.1724981112.0.0.0',
        '_shibsession_64656661756c7468747470733a2f2f6d79627573747564656e742e62752e6564752f73702f73686962626f6c657468': '_5ffb893c0b4026d1d5b74097de493ef2',
        'JSESSIONID': 'vuag4vFSXrKIMt5sxOqz3HYKVMPHgH3P!-655034622',
        'PS_TOKEN': 'pQAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4Abwg4AC4AMQAwABTtVLnGF4WEBxVlylhgKSMuAJVhumUAAAAFAFNkYXRhWXicHYdNDkAwFAZHiWVvoqGpv6UIYiMNEktHcEGH88VLvpl5D5ClJknk1/CfvdgYiKxM7OST3gUbOZg5uRlVwVPiCRRyJ3p6saLFqWuxkp2qoxFLjQ+XlgvM',
        'https%3a%2f%2fmybustudent.bu.edu%2fpsp%2fbuprd%2femployee%2fsa%2frefresh': 'list: %3ftab%3ddefault|%3frp%3ddefault|%3ftab%3dhpt_student_general_tab|%3frp%3dhpt_student_general_tab|%3ftab%3dhpt_student_academics_tab|%3frp%3dhpt_student_academics_tab|%3ftab%3dhpt_student_financials_tab|%3frp%3dhpt_student_financials_tab|%3ftab%3dremoteunifieddashboard|%3frp%3dremoteunifieddashboard',
        'CSRFCookie': '23c79966-aaac-4e21-a807-3c1972e87a30',
        'PS_TOKENEXPIRE': '30_Aug_2024_01:27:07_GMT',
    }

    headers = {
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': 'SignOnDefault=; hpt_institution=BU001; _opensaml_req_ss%3Amem%3Aca4e651a2dac6323407e6c8e6a1969db70691ec48571d95261acdd8aee982719=_638298e804531e6f6d31bf94fc9d16f6; uiscgi_prod=a8511dcdb8f7945cd1f4310cbde1d614:prod; _ga_8CFVMTVJ2Q=GS1.1.1723071785.1.1.1723071849.0.0.0; _opensaml_req_ss%3Amem%3Add2c81b400cea1b2c09b33b0df810367da19c83a0903252e9e3203b82f94e1ab=_e8323b5504681fe6e2ecc05df9a68efe; __utmc=21468840; _gac_UA-45347247-2=1.1723214024.Cj0KCQjwn7mwBhCiARIsAGoxjaJQ5KkqfCfc-_3e8nbBlAq3sGy07slqeZOgMHTagyoLcV8LOmvda7EaAqY9EALw_wcB; _gcl_aw=GCL.1723214024.Cj0KCQjwn7mwBhCiARIsAGoxjaJQ5KkqfCfc-_3e8nbBlAq3sGy07slqeZOgMHTagyoLcV8LOmvda7EaAqY9EALw_wcB; _gcl_dc=GCL.1723214024.Cj0KCQjwn7mwBhCiARIsAGoxjaJQ5KkqfCfc-_3e8nbBlAq3sGy07slqeZOgMHTagyoLcV8LOmvda7EaAqY9EALw_wcB; _gcl_gs=2.1.k1$i1723214021; _ga_QHQ86LM5JZ=GS1.1.1723214024.1.1.1723214469.57.0.0; _opensaml_req_ss%3Amem%3A6c54fe4550ff1f34247373850f02ecd72c7a7eab2f0169de67a9c66b8a7a5cf5=_2998b2a931067deaca4aedb1061fa281; _opensaml_req_ss%3Amem%3A030c25fba1fee8380a95ff626b4a657d921897abb862593d143f76deed5e8dd0=_226c712e82675b73c7a4bbba43e17061; _opensaml_req_ss%3Amem%3A846b8a7ae7752451eeb890a0c7d045d78131c739d1131fa0afab88d753f97bf7=_2861a9565a48abe6de58fe2ee051747b; _opensaml_req_ss%3Amem%3A875184bd6382b7a0618ce22c8ce3517d82dfb244ed8aff43d841ecf7b3f913f4=_196fe17180b238ddb9eb0c5c891c155f; _opensaml_req_ss%3Amem%3A54f1d3a06d8caedf420d18416724b07c3d01a6fbdd2230f1ea9c0cae2f0f2c99=_dbd280cbb14d70da0738dfda992ae112; _opensaml_req_ss%3Amem%3A3bb288a870e610700c7457801c2bd5018314fd0f3758b16a6057b37ae98e2104=_4ad4442e8592272e294c9c721bd109e1; _opensaml_req_ss%3Amem%3Af405b37ade3d8a99464cda1f246e32f87522c42b9567181c2dfdb65510ec4e60=_90ed58de656bd0758a060fc9b2983e7e; _opensaml_req_ss%3Amem%3A022b28964d940122405fc1741cf1a9acb4f408b86f7fcb43b53b3d614fa586ae=_e1751e0715ea9c807535f6133fea746d; _opensaml_req_ss%3Amem%3A97eff7ff4fd4ab9e83efbcf451f5a5d05bd7dad4df7dfb5605b1d2f0f2233f08=_8792ce7abc97695443c12d36093cbeb3; _opensaml_req_ss%3Amem%3A3541c826ee3ceaee65b0e06b65e1b09638e2f1ae8bf036a0a64b2c2c415e957f=_75f799f8ffdecb6cd74071fdb39a50f4; _opensaml_req_ss%3Amem%3Adabdab0cbca6f878079b99196752b07c5966918af1be0dcac1c48d6deac8cbfd=_409792138bdf35b585771268b75dab35; mybustudent-PORTAL-PSJSESSIONID=461be682d445cfd26ee479733657ebe2f30ee9e0; _opensaml_req_ss%3Amem%3Af38bd2447cbb9295603dec9578d1ae58a87473e4bd58fc6f3b9c5a90c944c31b=_395af84d49163f24a86c8f4c3b2a9e93; PS_LASTSITE=https://mybustudent.bu.edu/psp/BUPRD/; ExpirePage=https://mybustudent.bu.edu/psp/BUPRD/; PS_TokenSite=https://mybustudent.bu.edu/psp/BUPRD/?JSESSIONID; PS_LOGINLIST=https://mybustudent.bu.edu/BUPRD; ps_theme=node:SA portal:EMPLOYEE theme_id:BU_THEME_FLUID css:BU_THEME_FLUID_859 css_f:BU_GLOBAL_OVERRIDE_FL accessibility:N macroset:BU_DEFAULT_MACROSET_859 formfactor:3 piamode:2; PS_DEVICEFEATURES=width:1440 height:900 pixelratio:2 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0 maf:0; _ga_V91YQBS3LZ=GS1.1.1723831762.1.0.1723831838.0.0.0; _gcl_au=1.1.543065038.1723832235; _scid=35860a37-c3ca-44b6-b983-26bb54813388; _scid_r=35860a37-c3ca-44b6-b983-26bb54813388; _hjSessionUser_1849442=eyJpZCI6IjUxNjRmMjQyLWNlYzYtNTk2Ny05NmY0LTU4MzMwN2EzYzZmNyIsImNyZWF0ZWQiOjE3MjM4MzIyMzU5NzAsImV4aXN0aW5nIjp0cnVlfQ==; _fbp=fb.1.1723832236148.376725651588950729; _sctr=1%7C1723780800000; _ga_JGVBW8B4Z9=GS1.1.1723845318.2.0.1723845318.60.0.0; _ga_E08X766WBX=GS1.2.1724189740.1.0.1724189740.0.0.0; PS_TokenSite=https://public.mybustudent.bu.edu/psp/BUPRD/?public-PORTAL-PSJSESSIONID; _ga_NC4W1T8DC6=GS1.1.1724190127.1.1.1724190221.0.0.0; _ga_HVBYYX9KF6=GS1.1.1724198276.7.0.1724198276.0.0.0; _clck=1raffei%7C2%7Cfok%7C0%7C1696; _ga_PMCMRTPJSG=GS1.1.1724376383.1.1.1724376461.0.0.0; _ga_6VXTC1Y945=GS1.1.1724376382.1.1.1724376473.0.0.0; _ga_2V6PP6D2G4=GS1.1.1724710679.2.0.1724710679.0.0.0; __utma=21468840.1344430284.1722957096.1724190252.1724788829.6; __utmz=21468840.1724788829.6.5.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); _ga_0Z1EBE5RV7=GS1.1.1724788828.13.1.1724788871.0.0.0; _ga_WQG2H3DG4P=GS1.1.1724788829.1.1.1724788871.0.0.0; _opensaml_req_ss%3Amem%3A4e64223f5c6639edf0643f00ed7ae341c2a641a2ddf837bab5393c732c6c6a45=_9db25e03669015e4789702c85da060cf; _opensaml_req_ss%3Amem%3A36c837dcc9c004bdfdddb243afea056d392e411fd8a8122a62a2dce9f3a0b370=_de0144681571565e8dd067d0b2bf1208; _opensaml_req_ss%3Amem%3A9129019dc585039f276268cce34cc46167bbda27ac05a886f17180d8d6c648b5=_a4f851e7e947e7ee497f3697e4f2bdf3; _gid=GA1.2.1132378177.1724971981; _ga=GA1.1.1344430284.1722957096; _ga_L4SD8HKLDR=GS1.1.1724979673.3.0.1724979673.0.0.0; https%3a%2f%2fpublic.mybustudent.bu.edu%2fpsp%2fbuprd%2femployee%2fsa%2frefresh=list: %3ftab%3ddefault|%3frp%3ddefault|%3ftab%3dremoteunifieddashboard|%3frp%3dremoteunifieddashboard; nullemployee%2fsa%2frefresh=list: %3ftab%3drefresh_all_tabs; hpt_institution=BU001; CSRFCookie=f7d2e3ff-61a3-41aa-99a3-687c1889798c; public-PORTAL-PSJSESSIONID=XEmg4b7ZxhLqI9UDJhO_J8zkOc1Y8Gsg!1579944880; X-Oracle-BMC-LBS-Route=75f54d5ae18383bd0d20b006de3a209f3f6223e1e75e63566915a64c6ac704bcdc340990d42672cad21159007a251d416faef3cc67fe8210a8c699da; _ga_F7T3KG2073=GS1.1.1724981092.17.1.1724981112.0.0.0; _shibsession_64656661756c7468747470733a2f2f6d79627573747564656e742e62752e6564752f73702f73686962626f6c657468=_5ffb893c0b4026d1d5b74097de493ef2; JSESSIONID=vuag4vFSXrKIMt5sxOqz3HYKVMPHgH3P!-655034622; PS_TOKEN=pQAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4Abwg4AC4AMQAwABTtVLnGF4WEBxVlylhgKSMuAJVhumUAAAAFAFNkYXRhWXicHYdNDkAwFAZHiWVvoqGpv6UIYiMNEktHcEGH88VLvpl5D5ClJknk1/CfvdgYiKxM7OST3gUbOZg5uRlVwVPiCRRyJ3p6saLFqWuxkp2qoxFLjQ+XlgvM; https%3a%2f%2fmybustudent.bu.edu%2fpsp%2fbuprd%2femployee%2fsa%2frefresh=list: %3ftab%3ddefault|%3frp%3ddefault|%3ftab%3dhpt_student_general_tab|%3frp%3dhpt_student_general_tab|%3ftab%3dhpt_student_academics_tab|%3frp%3dhpt_student_academics_tab|%3ftab%3dhpt_student_financials_tab|%3frp%3dhpt_student_financials_tab|%3ftab%3dremoteunifieddashboard|%3frp%3dremoteunifieddashboard; CSRFCookie=23c79966-aaac-4e21-a807-3c1972e87a30; PS_TOKENEXPIRE=30_Aug_2024_01:27:07_GMT',
        'Referer': 'https://mybustudent.bu.edu/psc/BUPRD/EMPLOYEE/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_Main?acad_group=BU1',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',
        'accept': 'application/json',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
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
        'enrl_stat': '',
        'crse_attr': '',
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
    
    ### Uncomment to write to local file
    # with open('open_courses.txt', 'wb') as file:
    #     file.write(response.content)
    
    json_str = response.content.decode('utf-8')
    data = json.loads(json_str) 
    return ({"status": response.status_code, "body":data})

fetch_and_write_response()