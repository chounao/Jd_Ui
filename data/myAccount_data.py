class AccountPlatform:
    "账户平台页面信息"
    #关联记录class="link-record"
    associatedRecords_selectors = ['class','link-record']

    #主店铺框class="platform-item"
    shopModule_selectors = ['class','platform-item']

    #框内的按钮action-item
    moduleBtn_selectors = ['class','action-item']

    #下方默认位置记录取消关联按钮class="address-action"
    moduleBtns_selectors = ['class','address-action']

    #默认地址class="icon fhd-icon address-icon"
    defaultAddress_selectors = ['class','address-icon']

    #记录按钮class="icon fhd-icon record-icon"
    recordBtn_selectors = ['class','record-icon']

    #取消关联class="un-bind-item"
    disassociateBtn_selectors = ['class','un-bind-item']

    #关联按钮class="anticon anticon-plus-circle"
    correlationBtn_selectors = ['class','anticon-plus-circle']

    #悬浮class="ant-popover-open"
    bubblePage_selectors = ['class','ant-popover-open']