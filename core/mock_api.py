


def generate_mock(payload):
    print(payload)
    
    company_name = payload.get("company_name")
    parent_company = payload.get("parent_company")
    name = payload.get("name")
    id_card = payload.get("id_card")
    passport_no = payload.get("passport_no")
    
    amount_company = 0
    amount_case = 0
    license_id = None

    directorship_status = None
    lawsuits_status = None
    
    print(company_name)
    
    #case true true 
    if company_name == 'บจก. อยุธยา แคปปิตอล เซอร์วิสเซส':
        directorship_status = True
        lawsuits_status = True
        
        amount_company = 10
        amount_case = 8
        license_id = '0502822836872'
        
    #case true false
    elif company_name == 'บมจ. เงินติดล้อ (TIDLOR)':
        directorship_status = True
        lawsuits_status = False
        
        amount_company = 2
        amount_case = 1
        license_id = '0261720170468'
        
    #case false true
    elif company_name == 'บมจ. อิออน ธนสินทรัพย์ (ไทยแลนด์)':
        directorship_status = False
        lawsuits_status = True
        
        amount_company = 7
        amount_case = 9
        license_id = '0527818443313'
        
    #case false false 
    elif company_name == 'บจก. โตโยต้า ลีสซิ่ง (ประเทศไทย)':
        directorship_status = False
        lawsuits_status = False
        
        amount_company = 3
        amount_case = 7
        license_id = '0425036287570'
        
        
    #format output
    if directorship_status == False:
        directorship = 'ไม่พบการดำรงตำแหน่งบริษัทภายใต้การกำกับของ ธปท.'
    elif directorship_status == True:
        directorship = f'พบการดำรงตำแหน่งบริษัทภายใต้การกำกับของ ธปท. จำนวน {amount_company} บริษัท โดยสรุป'
        
    if lawsuits_status == False:
        lawsuits = 'ไม่พบการถูกฟ้องร้อง'
    elif lawsuits_status == True:
        lawsuits = f'พบการถูกฟ้องร้องจำนวน {amount_case} คดี โดยสรุป'

    license = f'บริษัท {company_name} และ บริษัทแม่ {parent_company} ได้รับ license {license_id} ภายใต้การกำกับของ ธปท.'
    
    return {"status": "success", 
            "company_name": company_name, 
            "parent_company": parent_company, 
            "name": name, 
            "id_card": id_card, 
            "passport_no": passport_no, 
            "flureg": 
                {"directorship": directorship,
                 "lawsuits": lawsuits,
                 "license": license
                }
            }
        
