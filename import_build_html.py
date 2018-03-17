import pandas as pd

str_records = """

<span style="color: #333399;">Dentist Directory Vancouver British Columbia is a one stop resource that offers a list of various dental clinics in Vancouver British Columbia. Find a particular dental practice in Vancouver British Columbia City related to:</span>

<span style="color: #333399;">General, family dentistry including preventative care, cavities, cleaning and whitening, cosmetic dentistry including dental implants, porcelain veneers, porcelain crowns and bridges.</span>

<span style="color: #ff6600;">You may further refine your search by using our search tool</span> <a href="http://www.dentistdirectorycanada.ca/11-2/">here</a>

<span style="color: #ff0000;">Advertising on Oral Health Local Services</span> <a href="http://www.dentistdirectorycanada.ca/contact-us/" target="_blank" rel="noopener">contact us</a>

[hr style="1" margin="20px"]
<strong>Find Dentists in Georgia </strong>
[hr style="1" margin="20px"]
"""




df_dentist=pd.read_csv('georgia_dentist_2.csv', dtype={'Website':str})
df_dentist=df_dentist.fillna(' ')
for i in range(int(len(df_dentist)/3)+1):
    record=df_dentist.iloc[i]
    str_first = "[one_third]\n<strong>" + str(record['Business Name']) + "</strong>\n" + str(record['Address']) + '\n' + str(record['City']) + ', ' + str(record['State']) + ' ' + str(record['Postal Code']) +\
                '\n' + 'Phone: ' + str(record['Phone Number']) + '\n<a href=' + str(record['Website']) + ">Website</a>" + '\n[/one_third]\n'
    record = df_dentist.iloc[i+1]
    str_second = "[one_third]\n<strong>" + str(record['Business Name']) + """</strong>
    """ + str(record['Address']) + '\n' + str(record['City']) + ', ' + str(record['State']) + ' ' + str(record['Postal Code']) +\
                '\n' + 'Phone: ' + str(record['Phone Number']) + '\n<a href=' + str(record['Website']) + ">Website</a>" + '\n[/one_third]\n'
    record = df_dentist.iloc[i + 2]
    str_third = "[one_third_last]\n<strong>" + str(record['Business Name']) + """</strong>
        """ + str(record['Address']) + '\n' + str(record['City']) + ', ' + str(record['State']) + ' ' + str(
        record['Postal Code']) + \
                 '\n' + 'Phone: ' + str(record['Phone Number']) + '\n' + "<a href="+str(
        record['Website'])+">Website</a>" + '\n[/one_third_last]' + '\n [hr style="1" margin="20px"] \n'

    str_records = str_records + '\n' + str_first+'\n'+str_second+'\n'+str_third


html_file = open('DDC_html_4.txt', 'w')
html_file.write(str_records)




html_file.close()