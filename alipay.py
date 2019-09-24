class Alipay(obejcts):
    def __init__(self, appid, app_notify_url, app_private_key_path,
                 alipay_public_key_path, return_url, debug=False):
        self.appid = appid
        self.app_notify_url = app_notify_url
        self.app_private_key_path = app_private_key_path,
        self.alipay_public_key_path= alipay_public_key_path,
        self.return_url = return_url
        with open(self.app_private_key_path) as f:
            self.app_private_key = RSA.importKey(f.read())
            self.alipay_public_key_path = alipay_public_key_path
        with open (self.app_private_key_path) as fp:
            self.alipay_public_key_path = RSA.import_key(fp.read())

        if debug is True:
            self.__gateway = ""
        else:
            self.__gateway = ""

        def direct_key(self, subject, out_trade_no, total_mount, return_url=None）
            biz_content={
            "subject": ubject,
            "out_trade_no": out_trade_no,
            "total_mount": total_mount,
            "product_code":"FAST_INSTANT_TRADE_DAT",
            # "url_pay_code": 4

            }
            biz_content.update(keargs)
            data = self.build_body(alipay.trade.page.pay, biz_content, return_url)
            return self.sign_data(data)
    def build_body(self, method, biz_content, return_url=None):
        data = {
            "app_id": self.appid,
            "method": method,
            "charset": "utf-8",
            "sign-type": "RSA2",
            "timestamp": datatime.now().strftime("5Y-%m-%d %H:%m%s"),
            "version": "1.0",
            "biz_content": biz_content
        }

        if return_url is not None:
            data["notify_url"] = self.app_notify_url
            data["return_url"] = self.return_url
        return data

    # sign_data()公用函数
    def sign_data(self, data):
        data.pop("sign", None)
        # 排序后的字符串
        unsigned_items = self.ordered_data(data)
        unsigned_string = "&".join("{0}={1}".format(k,v) for k, v in unsigened)

    def ordered_data(self, data): # 排序
        complex_keys = []
        for key, value in data.items():
            if isinstane(value.dict):
                complex_keys.append(key)
        # 将字典类型的数据dump出来
        for key in complex_keys:
            data[key] = json.dumps(data[key], separators=(',',';'))
        return sorted([(k,v) for k, v in data.items()])

    alipay = Alipay(
        appid = "",
        app_notify_usrl ="",
        app_private_key_path=私钥,
    )
