from cryptography.fernet import Fernet
import docx
cipher_key = 'ksQApEAl4YXr5NO1UnKmAPz0_ZtQlDv4FGChC_E1M4A='
cipher = Fernet(cipher_key)
def encryption(text:str) -> str:
    cryptoText = cipher.encrypt(text.encode('utf-8'))
    cryptoText = cryptoText.decode('utf-8')
    return cryptoText
    
def decryption (text:str) -> str:
    decrypted_text = cipher.decrypt(text.encode('utf-8'))
    decrypted_text = decrypted_text.decode('utf-8')
    return decrypted_text


#text = b'gAAAAABdvbGlTtNWKfcBHONn8-sI0K3pSsbDZYaSeapa82vSF-o-yV-vUxldp6HtXmzQHgpwiHuq4GyoECkvYAmcjAaLx8EkKgStsUFiHJNjLlNhp7r3eYaCI_9Q9Dt1lkw4v4a4g8Zkr2MwxdJdW2Koj4f97YC4eQaH1yh8PBjULViKEOJ8-wyGm3waPZNB6K_P1CU7OL8AK2_UiQCKPRz2McaGRu91MqiEs4EyBMnPi3fskASPfZWkC8-pKm_02dQCTsfXaP4xClPmaWWMAo6mtrspOMFbh83LtB4P0rDrQJ5fT6H7T_Q3Vpl-YY0CyDj20xF9I5om_iEw3tP68f9fxIP4D7Dab7Rm1PBQ4DCCE3owbEAWNVHVL5pgq5QhbVVjGNJ1TbY13HNXQckHRiWXsT7dbLFh5M-fnNh7EpEsPl_qt_6KvssTMhgUSiPGmxSJrga3n7sk7HUQC0iLei5GqiWk7XLHJ37lqQIaZkmdFl8oug3vzRttCvDs4Sl9UPGaP56bfsFa2m5ENLOrGPUVtbkAMWGzcKHOp1SHW2crHpOVVAWCZJJaUEj4Th6Il1PoQM2aJClCW63mW5BL7bNg26O0I9t8YzPGVlOceo-0AayvJQJijHjJNDxrzm2ySwv3Aptuc41sYDsRG_kbF5Xs-4Qii555lbxb74ZBXKL3AswczDA19pKlwbmnC9EtCHj57bJkjZGadwGcDzGaYS5sFGdEsxuHn68J0W8XGxLjknazQl7YIQvY2drXhQrFTX6XP34cYgZXTa9c1YtdLJUSOEnyNFCeOG71BnT5AcZJ7a1Yu9P1x2pp-nZCspEf3nRzhy-jgBlPrVmDdVCvWqyUpZWQ9w4UvDx7djN9rSuTG9YbDBThsO5XuocsPVUWtLZFkDE_Rw4WLZEaFxqUE7JWuyBAYcSbKdLzzuTlZqm0fQtx4RVSPViXVy1H0EeX35NgbPVaitQMYqYWmaAgw7nbcysjOnKVz_YRca2Drvuwe9lSkppEgxD6_bZehbD7p_PNAp_FNv3ofShD31kA52ZaK247XLPqFuNHgp3LFWOZRZqwxjH5bbaArEXD4b33OwQjqB_LdwRmFFuWh0gANLpaIlMS-VIzff_CWM_OdBUYs8y4T1am5n1wpw-Qj_tRlL9k4G-99AIL4XNfB5j8aCgT4ic3I7-nciz2k42nHvEVoTGank2Go2_NKdMYMj9ozQLDhABdNaM5icupnee5XwHFCjg98Jzd8vUTRl7D27IOdFlwHIoJlYcV2oqrArFWhFGb55XPvAovcl6TCEXZOEex3rAVkJLjkvlVdvwJzGwdUtr8wY2nd2zI9KCsuQSQKSjngRzYMzbV3P5otY8z9vMS5rVgQUrrCuqstn8YhH5IW2Xr6NueHbv2035UOh27y6IaEm01xa8hk9H6W8jmCPNSDxYOl6gbQxTTyP9WN0-ZL-P2IWiqVqJa8W6b0N25I8FWMB3eDipohTyrPt1iwm3vRHTULi_tOVBCuyyxoS7GlvE3_oZW0FnVRqHONTL6-dzOxHFqSptSQr6oUN1MaIQa2r5eLxu8L4eavV5gAvTsAZdeo67j8QQL9G0LCCozbUTU0dVyZgD_Klu_KmppkXrs0N6eQAOcVcEB-nCJ-SlahswpE1SvWlx5kdqF06mYwfSabDrnO-24PsuFemt4u4w2coMrqI4Krh0rY_tUbJfnFGCJUF9gCMuZS69r8zBEm0QAf-eRryZhSzHSVrWggPytnv1pF0xZuQmPlqLMEs87SjP90MTbczjh2TRUYTAj-IJcHnum7GVovR7EDBxXFRiE9EW55G-t5LkwkGB6g4256PhgfbFQX75dOyRg0lhjlNYa-AOavvlgw_7s_Eluw2MKkhcgK4-s5pPM5BlZdIpw2jsKP3oQ1QE3Hf4qBJlnQ096kYODpbuD60xGsp9WsbPhRuMJHwdDjviYcKFkoP8MtAbzjydjd2AI3yWJks-Qo_bDM7v7m9fUXuIj7arhzdKfu_qcDSEO_Qnnf6g_pUOCYlbwIDq9K8uIAT1D6kLOdpj2zUNdRg5XEDl6lrgnSIBX6i-0EpMCTx4gz62Q2knl_OkfhaJnVpEZ8eBLqq-yLMNvvhl1-Q10efxPmlNptedZudYCCwIYTMpa-04s4xvc0SUQRqMpIWDvs3vKx-O-gljF1O5PvTrK02iRHCpTx1m4WAROneW8cvYgJx0K4Q-YjEWR_aOGn_Azo4rtbuGncRHpK-A39-U4Kth-vXvFir6kID6QPMndgL6OHEo3H6y5wnCCqL2kQj5jPW5FbkkRLSPineIvFW5UhWa-qwTLa9wvyDS2I27KzjzGOeRCtFmf3Le08VW7aBCEXPJt0GU5oNMO0CvWX74IrkOwh3qHtX46QvZYMSVUGe0HL3S0hZsuxCe4-FIuqcD7WXZgOIoR4eoh5DDBDTPGfSAsZdNfEPGl03MOE8qeOAm5E_r8PMgN5IX4OU3Swdvj7hk3fe61XTTCoLoOhoB9cCeinA7S6ldjQjwU0vGopJHhYElNMqINSDrTpOkdiPIOfhoDg4gyQ7R7RYmoDjhLvXiWH2WcyQ9tMwWpHjpUP65d7MGW7P4Mz8eMLEX41wzFQ9RCVwYBglR1CWhk0v_EN4agMLMXgc_RxFUMmoOEckLjpVzHiM0SXfQes0JS8taJk_hhJkfXZ8_harOW4ae7Q6KAZgzlWwlmOHn48ZB1xi1-K6-LG4J4r8AMpsJt--pO7QJ4c3uHFv0g0aYChnLIDNX6jlJkzJvTWUIUmOAy1ZLWDswMpISQViaZ5RYJDs55ykVQDph-tdRb0J6M-62Sg9JfN5r22xnVpHCzKlWBPhyIIpm4UoONKEtlGlknJDR5Safib1W_CKKsyy5Ll8pPBr6A5ISu2QL8ojmfz7OXlyn4265m1Bw7JnfVvNQqBtOubnRlwyIVC_G5_Uu_f7AjBm9oybp7ztCWfEIjuoq7y_k5dpa0bdOxkUFrmqpKJsWZiejgJxnrfm3qoHWANjR6hwYwsNHUp6MXX-a_15itbKlgmQ8rwhtekxBRsnIlJPGZkLjxAOr8YI9DeDU8WiYYsB7e7JA7eQ3F8h9G3t0lbNVk-L72yRyt0qwE7xhSS672VfAldvRqZqayu226OBq5gUrnQDxubee5ZdxCl672L-SWuqC80Bl16zmfG74kOblgaHzQhWDqDjCF0mVpIFPfF8f6LzmN7muxvJRA1d8TLnQi6tX6prB2fCFG6UZMW6rqf0g172LdOkZMEZlwkaGsPKpbBfnCmWlmEPhCgfI7FTtIDuC2j8VWAXM9UbTImGZobDsOdMFh3CHm76DqiJEAGmHJf5_sJPaGkuzwaiJvxeVTKKEk8O3Pvjs9oHszhnsRk1QzfG0OUJTYIhL94R9UNsGp3RK6PsB5sJB_mSIOIqToE67TnZFNTwGIzoeQJqWOFZrUdasQBy_DSY4p4sTasyibKOks8TzWk8BK5I7ewOBurojsigVDz9_tXHVDl8-stVLhMbUOOevByyT-Gvp7P0wMsUj-tklBgY2U5XAsB5iHq58okL6oo9h7yJF4xCSw8dXA4pc6fGL3kKBJPut5uP-C7oVUrFbE8V-ZFrKR4Lajqjuxd3SYd7vF3UP1ByRcw66O3Mm-TU3QnQz0QC-Etj8cuCkxpAjcEEHU95gWljs7dofJpOrSN8zEesdiGpkMOh2XexnRiV_pbbqvGb9HoC0HtuNZ7B-7JGwgXQ7cqeT_o7FFOp0FZTDkpvHGsmIbnYSfNOmXMS4od67jsOIPh-IVHFIFNR-vPnkoTYJizv_qSY7sm_zK6iVkg-mxdkHkQmFzZpMV__YAN1si6Fd5DcBuXydghNuAanrk7UCosMghrLpOeD0Q4lGneLL5I0bcFZ6_vuODyEInWD_nUnLs-ha1pucSQknl4m-7_EZHNrja1r1Sb_mFxuRMI4hf4BjpJvJpA52UQBxiytOaH-GHJvU98IhcSI0nNcp7f_YElol5-9e4nwtBdnJmrCAasYO9_v5VZaQOs9EDie3kt6BCTQY8hoY0y-rmhHSTHg6hgdEV8-BTSm9LqluHM3biGhBUbCu9w23OkLyJXkxiAmjX9HHoWfjydthFWMrc1Y4Cz5HflhudU1HbWLJ4qhnBo0YJkMTe55lCPenBDqg8TltgrLTZc2Er625LZdzac-zkoPMZQga3dKK9MxQfj6vQ0gATdnKE1H71rWwYL1Pzj6_atBkrWc7FDfExNJSfX3Rh86HfoqTzL6P5QKhWG4gMVc7gKqGDCGSt4aRl8cT21eSVz7EPJs7OelN3lt2RpM5-EY1kIG4csg1tVyDSrvx8fuU='
#doc = docx.Document(r'C:\Users\Z580\Desktop\ш.docx')
#text = ''
#for paragraph in doc.paragraphs:
    #text += paragraph.text + '\n'
#print(type(text.encode('utf-8')))
#text.encode('utf-8')
#print(text.encode('utf-8'))
#print(type(text))
#print(decryption(text))
#doc.core_properties.author = 'Hello'
#doc.save('i.docx')
#print(doc.core_properties.author)
#string = 'dfgdg'
#if not string:
  # print(True)