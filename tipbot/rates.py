import requests


RATE_API = 'https://www.bitcoin.com/special/rates.json'
CURRENCY_CODE = {
    'AED': 0,
    'AFN': 1,
    'ALL': 2,
    'AMD': 3,
    'ANG': 4,
    'AOA': 5,
    'ARS': 6,
    'AUD': 7,
    'AWG': 8,
    'AZN': 9,
    'BAM': 10,
    'BBD': 11,
    'BCH_BTC': 12,
    'BDT': 13,
    'BGN': 14,
    'BHD': 15,
    'BIF': 16,
    'BMD': 17,
    'BND': 18,
    'BOB': 19,
    'BRL': 20,
    'BSD': 21,
    'BTN': 22,
    'BWP': 23,
    'BYN': 24,
    'BZD': 25,
    'CAD': 26,
    'CDF': 27,
    'CHF': 28,
    'CLF': 29,
    'CLP': 30,
    'CNY': 31,
    'COP': 32,
    'CRC': 33,
    'CUP': 34,
    'CVE': 35,
    'CZK': 36,
    'DJF': 37,
    'DKK': 38,
    'DOP': 39,
    'DZD': 40,
    'EGP': 41,
    'ETB': 42,
    'ETH': 43,
    'EUR': 44,
    'FJD': 45,
    'FKP': 46,
    'GBP': 47,
    'GEL': 48,
    'GHS': 49,
    'GIP': 50,
    'GMD': 51,
    'GNF': 52,
    'GTQ': 53,
    'GUSD': 54,
    'GYD': 55,
    'HKD': 56,
    'HNL': 57,
    'HRK': 58,
    'HTG': 59,
    'HUF': 60,
    'IDR': 61,
    'ILS': 62,
    'INR': 63,
    'IQD': 64,
    'IRR': 65,
    'ISK': 66,
    'JEP': 67,
    'JMD': 68,
    'JOD': 69,
    'JPY': 70,
    'KES': 71,
    'KGS': 72,
    'KHR': 73,
    'KMF': 74,
    'KPW': 75,
    'KRW': 76,
    'KWD': 77,
    'KYD': 78,
    'KZT': 79,
    'LAK': 80,
    'LBP': 81,
    'LKR': 82,
    'LRD': 83,
    'LSL': 84,
    'LYD': 85,
    'MAD': 86,
    'MDL': 87,
    'MGA': 88,
    'MKD': 89,
    'MMK': 90,
    'MNT': 91,
    'MOP': 92,
    'MRU': 93,
    'MUR': 94,
    'MVR': 95,
    'MWK': 96,
    'MXN': 97,
    'MYR': 98,
    'MZN': 99,
    'NAD': 100,
    'NGN': 101,
    'NIO': 102,
    'NOK': 103,
    'NPR': 104,
    'NZD': 105,
    'OMR': 106,
    'PAB': 107,
    'PAX': 108,
    'PEN': 109,
    'PGK': 110,
    'PHP': 111,
    'PKR': 112,
    'PLN': 113,
    'PYG': 114,
    'QAR': 115,
    'RON': 116,
    'RSD': 117,
    'RUB': 118,
    'RWF': 119,
    'SAR': 120,
    'SBD': 121,
    'SCR': 122,
    'SDG': 123,
    'SEK': 124,
    'SGD': 125,
    'SHP': 126,
    'SLL': 127,
    'SOS': 128,
    'SRD': 129,
    'STN': 130,
    'SVC': 131,
    'SYP': 132,
    'SZL': 133,
    'THB': 134,
    'TJS': 135,
    'TMT': 136,
    'TND': 137,
    'TOP': 138,
    'TRY': 139,
    'TTD': 140,
    'TWD': 141,
    'TZS': 142,
    'UAH': 143,
    'UGX': 144,
    'USD': 145,
    'USDC': 146,
    'UYU': 147,
    'UZS': 148,
    'VEF': 149,
    'VES': 150,
    'VND': 151,
    'VUV': 152,
    'WST': 153,
    'XAF': 154,
    'XAG': 155,
    'XAU': 156,
    'XCD': 157,
    'XOF': 158,
    'XPF': 159,
    'XRP': 160,
    'YER': 161,
    'ZAR': 162,
    'ZMW': 163,
    'ZWL': 164,
    'BCC': 165,
    'BCH': 166,
    'BTC': 167,
}


def get_rate(update, currency='USD'):
    """ Returns the BCH price fetching Bitcoin.com API """
    currency = currency.upper()
    if currency not in CURRENCY_CODE:
        return update.message.reply_text(f'{currency} is not a supported '
                                         'currency.')
    r = requests.get(RATE_API)
    if r.status_code != 200:
        return update.message.reply_text(f'Unable to contact {RATE_API}')
    data = r.json()
    currency_btc_rate = data[CURRENCY_CODE[currency]]['rate']
    bch_btc_rate = data[CURRENCY_CODE['BCH_BTC']]['rate']
    return currency_btc_rate / bch_btc_rate
