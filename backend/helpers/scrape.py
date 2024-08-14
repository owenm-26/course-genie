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
        '_ga': 'GA1.1.1344430284.1722957096',
        '__utma': '21468840.1344430284.1722957096.1723213990.1723426228.3',
        '__utmz': '21468840.1723426228.3.3.utmcsr=email_20240809_full_weekly|utmccn=bu_today|utmcmd=2_must_read_5|utmcct=faculty',
        '_opensaml_req_ss%3Amem%3A6c54fe4550ff1f34247373850f02ecd72c7a7eab2f0169de67a9c66b8a7a5cf5': '_2998b2a931067deaca4aedb1061fa281',
        '_opensaml_req_ss%3Amem%3A030c25fba1fee8380a95ff626b4a657d921897abb862593d143f76deed5e8dd0': '_226c712e82675b73c7a4bbba43e17061',
        '_opensaml_req_ss%3Amem%3A846b8a7ae7752451eeb890a0c7d045d78131c739d1131fa0afab88d753f97bf7': '_2861a9565a48abe6de58fe2ee051747b',
        '_ga_0Z1EBE5RV7': 'GS1.1.1723493897.5.0.1723493897.0.0.0',
        '_ga_HVBYYX9KF6': 'GS1.1.1723493897.4.0.1723493897.0.0.0',
        '_opensaml_req_ss%3Amem%3A875184bd6382b7a0618ce22c8ce3517d82dfb244ed8aff43d841ecf7b3f913f4': '_196fe17180b238ddb9eb0c5c891c155f',
        'mybustudent-PORTAL-PSJSESSIONID': 'd21b1c215171f121974f4ee518de5735f4adbd2b',
        '_opensaml_req_ss%3Amem%3A54f1d3a06d8caedf420d18416724b07c3d01a6fbdd2230f1ea9c0cae2f0f2c99': '_dbd280cbb14d70da0738dfda992ae112',
        'ExpirePage': 'https://mybustudent.bu.edu/psp/BUPRD/',
        'PS_LOGINLIST': 'https://mybustudent.bu.edu/BUPRD',
        'PS_LASTSITE': 'https://mybustudent.bu.edu/psp/BUPRD/',
        'ps_theme': 'node:SA portal:EMPLOYEE theme_id:BU_THEME_FLUID css:BU_THEME_FLUID_859 css_f:BU_GLOBAL_OVERRIDE_FL accessibility:N macroset:BU_DEFAULT_MACROSET_859 formfactor:3 piamode:2',
        'PS_DEVICEFEATURES': 'width:1440 height:900 pixelratio:2 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0 maf:0',
        '_opensaml_req_ss%3Amem%3A3bb288a870e610700c7457801c2bd5018314fd0f3758b16a6057b37ae98e2104': '_4ad4442e8592272e294c9c721bd109e1',
        '_opensaml_req_ss%3Amem%3Af405b37ade3d8a99464cda1f246e32f87522c42b9567181c2dfdb65510ec4e60': '_90ed58de656bd0758a060fc9b2983e7e',
        '_opensaml_req_ss%3Amem%3A022b28964d940122405fc1741cf1a9acb4f408b86f7fcb43b53b3d614fa586ae': '_e1751e0715ea9c807535f6133fea746d',
        '_ga_F7T3KG2073': 'GS1.1.1723604906.11.1.1723604944.0.0.0',
        '_shibsession_64656661756c7468747470733a2f2f6d79627573747564656e742e62752e6564752f73702f73686962626f6c657468': '_7a497cac3c6d6441d74b0feb68c3dc32',
        'JSESSIONID': 'YgVO3ElXDeg3gdE4fVPIKBic_pfV8QuC!-1213897366',
        'PS_TOKEN': 'pQAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4Abwg4AC4AMQAwABTVyoNAe9x2GePYMHO0HNdCF4urlGUAAAAFAFNkYXRhWXicJYpBDkAwFERfEUs3IVqNsBQpsZEGiaUjuKDDmTCL9/6fzA1kaWKM/CR8KU5WBiILgY086J0pIjsTBxejLu+ocXhKuRMtzceeSs1PL7ay1dJpxQuWmAvA',
        'PS_TokenSite': 'https://mybustudent.bu.edu/psp/BUPRD/?JSESSIONID',
        'https%3a%2f%2fmybustudent.bu.edu%2fpsp%2fbuprd%2femployee%2fsa%2frefresh': 'list: %3ftab%3ddefault|%3frp%3ddefault|%3ftab%3dhpt_student_general_tab|%3frp%3dhpt_student_general_tab|%3ftab%3dhpt_student_academics_tab|%3frp%3dhpt_student_academics_tab|%3ftab%3dhpt_student_financials_tab|%3frp%3dhpt_student_financials_tab|%3ftab%3dremoteunifieddashboard|%3frp%3dremoteunifieddashboard',
        'CSRFCookie': '94fd8658-5ecd-441d-a5e3-7d3a9eb3bbff',
        'PS_TOKENEXPIRE': '14_Aug_2024_03:11:09_GMT',
    }

    headers = {
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        # 'Cookie': 'SignOnDefault=; hpt_institution=BU001; _opensaml_req_ss%3Amem%3Aca4e651a2dac6323407e6c8e6a1969db70691ec48571d95261acdd8aee982719=_638298e804531e6f6d31bf94fc9d16f6; uiscgi_prod=a8511dcdb8f7945cd1f4310cbde1d614:prod; _ga_8CFVMTVJ2Q=GS1.1.1723071785.1.1.1723071849.0.0.0; _opensaml_req_ss%3Amem%3Add2c81b400cea1b2c09b33b0df810367da19c83a0903252e9e3203b82f94e1ab=_e8323b5504681fe6e2ecc05df9a68efe; __utmc=21468840; _gac_UA-45347247-2=1.1723214024.Cj0KCQjwn7mwBhCiARIsAGoxjaJQ5KkqfCfc-_3e8nbBlAq3sGy07slqeZOgMHTagyoLcV8LOmvda7EaAqY9EALw_wcB; _gcl_aw=GCL.1723214024.Cj0KCQjwn7mwBhCiARIsAGoxjaJQ5KkqfCfc-_3e8nbBlAq3sGy07slqeZOgMHTagyoLcV8LOmvda7EaAqY9EALw_wcB; _gcl_dc=GCL.1723214024.Cj0KCQjwn7mwBhCiARIsAGoxjaJQ5KkqfCfc-_3e8nbBlAq3sGy07slqeZOgMHTagyoLcV8LOmvda7EaAqY9EALw_wcB; _gcl_gs=2.1.k1$i1723214021; _ga_QHQ86LM5JZ=GS1.1.1723214024.1.1.1723214469.57.0.0; _ga=GA1.1.1344430284.1722957096; __utma=21468840.1344430284.1722957096.1723213990.1723426228.3; __utmz=21468840.1723426228.3.3.utmcsr=email_20240809_full_weekly|utmccn=bu_today|utmcmd=2_must_read_5|utmcct=faculty; _opensaml_req_ss%3Amem%3A6c54fe4550ff1f34247373850f02ecd72c7a7eab2f0169de67a9c66b8a7a5cf5=_2998b2a931067deaca4aedb1061fa281; _opensaml_req_ss%3Amem%3A030c25fba1fee8380a95ff626b4a657d921897abb862593d143f76deed5e8dd0=_226c712e82675b73c7a4bbba43e17061; _opensaml_req_ss%3Amem%3A846b8a7ae7752451eeb890a0c7d045d78131c739d1131fa0afab88d753f97bf7=_2861a9565a48abe6de58fe2ee051747b; _ga_0Z1EBE5RV7=GS1.1.1723493897.5.0.1723493897.0.0.0; _ga_HVBYYX9KF6=GS1.1.1723493897.4.0.1723493897.0.0.0; _opensaml_req_ss%3Amem%3A875184bd6382b7a0618ce22c8ce3517d82dfb244ed8aff43d841ecf7b3f913f4=_196fe17180b238ddb9eb0c5c891c155f; mybustudent-PORTAL-PSJSESSIONID=d21b1c215171f121974f4ee518de5735f4adbd2b; _opensaml_req_ss%3Amem%3A54f1d3a06d8caedf420d18416724b07c3d01a6fbdd2230f1ea9c0cae2f0f2c99=_dbd280cbb14d70da0738dfda992ae112; ExpirePage=https://mybustudent.bu.edu/psp/BUPRD/; PS_LOGINLIST=https://mybustudent.bu.edu/BUPRD; PS_LASTSITE=https://mybustudent.bu.edu/psp/BUPRD/; ps_theme=node:SA portal:EMPLOYEE theme_id:BU_THEME_FLUID css:BU_THEME_FLUID_859 css_f:BU_GLOBAL_OVERRIDE_FL accessibility:N macroset:BU_DEFAULT_MACROSET_859 formfactor:3 piamode:2; PS_DEVICEFEATURES=width:1440 height:900 pixelratio:2 touch:0 geolocation:1 websockets:1 webworkers:1 datepicker:1 dtpicker:1 timepicker:1 dnd:1 sessionstorage:1 localstorage:1 history:1 canvas:1 svg:1 postmessage:1 hc:0 maf:0; _opensaml_req_ss%3Amem%3A3bb288a870e610700c7457801c2bd5018314fd0f3758b16a6057b37ae98e2104=_4ad4442e8592272e294c9c721bd109e1; _opensaml_req_ss%3Amem%3Af405b37ade3d8a99464cda1f246e32f87522c42b9567181c2dfdb65510ec4e60=_90ed58de656bd0758a060fc9b2983e7e; _opensaml_req_ss%3Amem%3A022b28964d940122405fc1741cf1a9acb4f408b86f7fcb43b53b3d614fa586ae=_e1751e0715ea9c807535f6133fea746d; _ga_F7T3KG2073=GS1.1.1723604906.11.1.1723604944.0.0.0; _shibsession_64656661756c7468747470733a2f2f6d79627573747564656e742e62752e6564752f73702f73686962626f6c657468=_7a497cac3c6d6441d74b0feb68c3dc32; JSESSIONID=YgVO3ElXDeg3gdE4fVPIKBic_pfV8QuC!-1213897366; PS_TOKEN=pQAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4Abwg4AC4AMQAwABTVyoNAe9x2GePYMHO0HNdCF4urlGUAAAAFAFNkYXRhWXicJYpBDkAwFERfEUs3IVqNsBQpsZEGiaUjuKDDmTCL9/6fzA1kaWKM/CR8KU5WBiILgY086J0pIjsTBxejLu+ocXhKuRMtzceeSs1PL7ay1dJpxQuWmAvA; PS_TokenSite=https://mybustudent.bu.edu/psp/BUPRD/?JSESSIONID; https%3a%2f%2fmybustudent.bu.edu%2fpsp%2fbuprd%2femployee%2fsa%2frefresh=list: %3ftab%3ddefault|%3frp%3ddefault|%3ftab%3dhpt_student_general_tab|%3frp%3dhpt_student_general_tab|%3ftab%3dhpt_student_academics_tab|%3frp%3dhpt_student_academics_tab|%3ftab%3dhpt_student_financials_tab|%3frp%3dhpt_student_financials_tab|%3ftab%3dremoteunifieddashboard|%3frp%3dremoteunifieddashboard; CSRFCookie=94fd8658-5ecd-441d-a5e3-7d3a9eb3bbff; PS_TOKENEXPIRE=14_Aug_2024_03:11:09_GMT',
        'Referer': 'https://mybustudent.bu.edu/psc/BUPRD/EMPLOYEE/SA/s/WEBLIB_HCX_CM.H_CLASS_SEARCH.FieldFormula.IScript_Main?',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
        'accept': 'application/json',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
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
        'acad_group': '',
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