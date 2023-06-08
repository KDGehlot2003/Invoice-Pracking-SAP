from twocaptcha import TwoCaptcha

solver = TwoCaptcha('edf9f7fc070b2e9f3bb2bed15f950152')

config = {
            'server':           '2captcha.com',
            'apiKey':           'edf9f7fc070b2e9f3bb2bed15f950152',
            'softId':            123,
            'callback':         'https://your.site/result-receiver',
            'defaultTimeout':    120,
            'recaptchaTimeout':  600,
            'pollingInterval':   10,
        }
solver = TwoCaptcha(**config)


result = solver.normal('get-captcha-image.jpeg')

print(result)