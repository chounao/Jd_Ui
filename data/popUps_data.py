class PopupNotification:
    ''' 新人引导部分'''
    # 新人引导后的弹窗属性class="guide-modal guide-modal-class"
    Newcomer_popup_selectors = ['class','guide-modal.guide-modal-class']
    # 新人引导上的字段class="guide-content" 您已经完成新人引导
    Newcomer_content_selectors = ['class','guide-content']
    # 新人引导我知道了class="guide-modal-footer-btn "我知道啦
    Newcomer_closeBtn_selectors = ['class','guide-modal-footer-btn']

    ''' 到期公告'''
    #弹窗class="ant-modal-body"
    ad_selectors = ['class','ant-modal-body']
    #关闭弹窗class="ant-modal-close-x"
    ad_closeBtn_selectors = ['class','ant-modal-close-x']


    """所有使用ant-modal-content的弹窗的元素都在这写"""
    # 弹窗class="ant-modal-content"
    popUp_selectors = ['class','ant-modal-content']

    # 关闭按钮class="ant-modal-close"【x按钮】
    closeBtn_selectors = ['class','ant-modal-close']

    # 账户平台/地址设置/确认按钮class="shipping-address-window-footer-ok-btn"
    confirmBtn1_selectors =['class','shipping-address-window-footer-ok-btn']

    # 账户平台/订购记录确认按钮ant-btn-primary【关联记录，解除绑定确定】
    confirmBtn2_selectors = ['class','ant-btn-primary']

    # 取消按钮class="ant-btn"
    CancelBtn_selectors = ['class','ant-btn']

    # 地址弹窗默认按钮class="action-item"
    setAddres_selectors = ['class','action-item']

    # 新建寄件地址class="add-new-shipping"
    addShipping_selectors = ['class','add-new-shipping']

    # 设置双地址预计弹窗上的
    # 预警开关class="ant-switch ant-switch-checked"


