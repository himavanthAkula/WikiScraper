'''l1={'Telangana':1,'Andhra-Pradesh':2,'Hyderabad':3}
l3={'ADILABAD': 25, 'BHADRADRI KOTHAGUDEM': 26, 'CYBERABAD': 239, 'HYDERABAD': 27, 'JAGTIAL': 28, 'JANGAON': 29, 'JAYASHANKAR BHUPALPALLY': 30, 'JOGULAMBA GADWAL': 31, 'KAMAREDDY': 32, 'KARIMNAGAR': 33, 'KHAMMAM': 34, 'KUMURAM BHEEM': 35, 'MAHABUBABAD': 36, 'MAHABUBNAGAR': 37, 'MANCHERIAL': 38, 'MEDAK': 39, 'MULUGU': 275, 'NAGARKURNOOL': 40, 'NALGONDA': 41, 'NARAYANPET': 301, 'NIRMAL': 42, 'NIZAMABAD': 43, 'PEDDAPALLE': 44, 'RAJANNA SIRCILLA': 45, 'SANGAREDDY': 46, 'SECUNDERABAD': 238, 'SIDDIPET': 47, 'SURYAPET': 48, 'VIKARABAD': 49, 'WANAPARTHY': 50, 'WARANGAL': 51, 'WARANGAL GRAMEENAM': 52, 'YADADRI BHUVANAGIRI': 53}
l2={'AMARAVATI': 6, 'ANANTAPUR': 7, 'CHITTOOR': 8, 'EAST GODAVARI': 9, 'GUNTUR CITY': 10, 'GUNTUR RURAL': 11, 'KADAPA': 12,  'KRISHNA': 14, 'KURNOOL': 15, 'NELLORE': 16, 'PRAKASAM': 18, 'SRIKAKULAM': 19,  'VISAKHAPATNAM': 21, 'VISAKHAPATNAM CITY': 22, 'VIZIANAGARAM': 23, 'WEST GODAVARI': 24}
k1=list(l1.keys())
k3=list(l3.keys())
k2=list(l2.keys())
no=0
matter=''
while True:
	if ((no>len(k1))&(no>len(k2))&(no>len(k3))):
		print(no)
		break
	word1=''
	word2=''
	word3=''
	link3=''
	link2=''
	link1=''
	try:
		word3=k3[no]
		link3="https://garudadev.herokuapp.com/eenadu/"+str(l3[word3])+"/"+word3.replace(' ','-')+"/40"
		word3='<button style="color:black;font-size:35;width:400px;height:50px;">'+word3+"</button>"
		word2=k2[no]
		link2="https://garudadev.herokuapp.com/eenadu/"+str(l2[word2])+"/"+word2.replace(' ','-')+"/40"
		word2='<button style="color:black;font-size:35;width:400px;height:50px;">'+word2+"</button>"
		word1=k1[no]
		link1="https://garudadev.herokuapp.com/eenadu/"+str(l1[word1])+"/"+word1.replace(' ','-')+"/40"
		word1='<button style="color:black;font-size:35;width:400px;height:50px;">'+word1+"</button>"	
	except Exception:
		pass
	matter+="<tr><td><a href="+link1+">"+word1+"</a></td><td><a href="+link2+">"+word2+"</a></td><td><a href="+link3+">"+word3+"</a></td></tr>"
	no+=1
print(matter)'''
import requests
from bs4 import BeautifulSoup
import json

	
def WikiData(link):
	res=requests.get(link).text
	res=res.replace('<br />',' <br />')
	soup=BeautifulSoup(res,'lxml')
	finder1=soup.find(class_='infobox vcard')
	finder1=soup.findAll('tr')
	data={}
	for i in finder1:
		name=i.find('th')
		if (name!=None):
			try:
				data[name.text]=i.find('td').text
			except Exception:
				pass
	return data

def LonLat(address):
	res=requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+address+"&key=AIzaSyDyb0_iNF_gpoxydk5Vd8IpWj1Hy1Tp5Vc").json()
	return [res["results"][0]["formatted_address"],res["results"][0]["geometry"]["location"]]


def ParseTable():
	res = requests.get("https://en.wikipedia.org/wiki/Union_Council_of_Ministers").text
	soup = BeautifulSoup(res,'lxml')
	data1=(soup.findAll('table')[3]).findAll('tr')	
	data={}
	for i in data1:
		try:
			j=i.findAll("td")[2]
			data[j.text.replace('\n','')]=j.find('a')['href']
		except Exception as e:
			pass
	return data

cabinet_ministers={"Narendra Modi": ["Vadnagar, Gujarat, India", {"lat": 23.7757259, "lng": 72.6165643}], "Rajnath Singh": ["Bhabhaura, Chakia, Uttar Pradesh 232103, India", {"lat": 25.0492119, "lng": 83.2211538}], "Amit Shah": ["Mumbai, Maharashtra, India", {"lat": 19.0759837, "lng": 72.8776559}], "Nirmala Sitharaman": ["Madurai, Tamil Nadu, India", {"lat": 9.9252007, "lng": 78.1197754}], "Subrahmanyam Jaishankar": ["New Delhi, Delhi, India", {"lat": 28.6139391, "lng": 77.2090212}], "Nitin Gadkari": ["Nagpur, Maharashtra, India", {"lat": 21.1458004, "lng": 79.0881546}], "Smriti Irani": ["New Delhi, Delhi, India", {"lat": 28.6139391, "lng": 77.2090212}], "Piyush Goyal": ["Mumbai, Maharashtra, India", {"lat": 19.0759837, "lng": 72.8776559}], "D. V. Sadananda Gowda": ["Sullia, Karnataka, India", {"lat": 12.5580735, "lng": 75.3907667}], "Arjun Munda": ["Jamshedpur, Jharkhand, India", {"lat": 22.8045665, "lng": 86.2028754}], "Harsimrat Kaur Badal": ["New Delhi, Delhi, India", {"lat": 28.6139391, "lng": 77.2090212}], "Ram Vilas Paswan": ["Khagaria, Bihar, India", {"lat": 25.50452, "lng": 86.47014159999999}], "Ravi Shankar Prasad": ["Patna, Bihar, India", {"lat": 25.5940947, "lng": 85.1375645}], "Dharmendra Pradhan": ["Talcher, Odisha, India", {"lat": 20.9501027, "lng": 85.216816}], "Narendra Singh Tomar": ["Morar, Gwalior, Madhya Pradesh, India", {"lat": 26.2186123, "lng": 78.22192249999999}], "Thawar Chand Gehlot": ["Nagda, Madhya Pradesh, India", {"lat": 23.4561435, "lng": 75.42266649999999}], "Ramesh Pokhriyal": ["Pinani, Uttarakhand, India", {"lat": 30.0257068, "lng": 78.9217522}], "Harsh Vardhan": ["Delhi, India", {"lat": 28.7040592, "lng": 77.10249019999999}], "Prakash Javdekar": ["69, Mumbai - Pune Hwy, Shivneri Nagar, Govandi East, Mumbai, Maharashtra 400088, India", {"lat": 19.0515413, "lng": 72.9107251}], "Mukhtar Abbas Naqvi": ["Prayagraj, Uttar Pradesh, India", {"lat": 25.4358011, "lng": 81.846311}], "Mahendra Nath Pandey": ["Ghazipur,Uttar Pradesh, India", {"lat": 25.6107088, "lng": 83.5701592}], "Pralhad Joshi": ["Vijayapura, Karnataka, India", {"lat": 16.8301708, "lng": 75.710031}], "Gajendra Singh Shekhawat": ["Jaisalmer, Rajasthan 345001, India", {"lat": 26.9157487, "lng": 70.9083443}], "Giriraj Singh": ["Barahiya, Bihar 811302, India", {"lat": 25.2835533, "lng": 86.0172595}],"Santosh Gangwar": ["Bareilly, Uttar Pradesh, India", {"lat": 28.3670355, "lng": 79.4304381}], "Rao Inderjit Singh": ["Rewari, Haryana 123401, India", {"lat": 28.1919738, "lng": 76.6190774}], "Shripad Yesso Naik": ["Adpai, Goa 403401, India", {"lat": 15.3747012, "lng": 73.9697795}], "Dr. Jitendra Singh": ["Jammu", {"lat": 32.7266016, "lng": 74.8570259}], "Kiren Rijiju": ["Nafra 790001", {"lat": 27.3723244, "lng": 92.54579539999999}], "Prahlad Singh Patel": ["Narsinghpur, Madhya Pradesh, India", {"lat": 22.9473179, "lng": 79.1923266}], "Raj Kumar Singh": ["Supaul, Bihar 852131, India", {"lat": 26.1233718, "lng": 86.6045134}], "Hardeep Singh Puri": ["Delhi, India", {"lat": 28.7040592, "lng": 77.10249019999999}], "Mansukh L. Mandaviya": ["Hanol, Gujarat 364230, India", {"lat": 21.6229681, "lng": 71.7511269}],"Faggan Singh Kulaste": ["Mandla, Madhya Pradesh, India", {"lat": 22.5979218, "lng": 80.3713855}], "Ashwini Kumar Choubey": ["Bhagalpur, Bihar, India", {"lat": 24.9506738, "lng": 87.11984149999999}], "Arjun Ram Meghwal": ["Bikaner, Rajasthan, India", {"lat": 28.0229348, "lng": 73.3119159}], "V. K. Singh": ["Pune, Maharashtra, India", {"lat": 18.5204303, "lng": 73.8567437}], "Krishan Pal Gurjar": ["Faridabad, Haryana, India", {"lat": 28.4089123, "lng": 77.3177894}], "Raosaheb Danve": ["Jalna, Maharashtra, India", {"lat": 19.8346659, "lng": 75.88163449999999}], "G. Kishan Reddy": ["Thimmapur, Telangana 509325, India", {"lat": 17.1678509, "lng": 78.2982782}], "Parshottam Rupala": ["Amreli, Gujarat 365601, India", {"lat": 21.6015242, "lng": 71.2203555}], "Ramdas Athawale": ["Agalgaon, Maharashtra 416403, India", {"lat": 17.0871483, "lng": 74.9153967}], "Sadhvi Niranjan Jyoti": ["Patewar, Uttar Pradesh, India", {"lat": 24.9054901, "lng": 82.67804629999999}], "Babul Supriyo": ["Uttarpara, West Bengal, India", {"lat": 22.6700938, "lng": 88.3354998}], "Sanjeev Kumar Balyan": ["Kutbi Kutba, Uttar Pradesh, India", {"lat": 29.4035148, "lng": 77.5327095}], "Sanjay Shamrao Dhotre": ["Akola, Maharashtra, India", {"lat": 20.7002159, "lng": 77.0081678}], "Anurag Thakur": ["Hamirpur, Himachal Pradesh, India", {"lat": 31.6861745, "lng": 76.52130919999999}], "Suresh Angadi": ["Kondas Koppa, Karnataka 590020, India", {"lat": 15.7997864, "lng": 74.5682972}], "Nityanand Rai": ["Hajipur, Bihar, India", {"lat": 25.6924354, "lng": 85.20832399999999}], "Rattan Lal Kataria": ["Sandhla, Haryana 135133, India", {"lat": 29.9824245, "lng": 77.21526279999999}], "V. Muraleedharan": ["Thalassery, Kerala, India", {"lat": 11.7491424, "lng": 75.4890346}], "Renuka Singh": ["Koriya, Chhattisgarh, India", {"lat": 23.3875499, "lng": 82.38857829999999}], "Som Parkash": ["Daulatpur, Punjab 144516, India", {"lat": 31.1031192, "lng": 76.2116987}], "Rameswar Teli": ["Duliajan, Assam, India", {"lat": 27.3572121, "lng": 95.3222503}], "Pratap Chandra Sarangi": ["Gopinathpur, Odisha 756040, India", {"lat": 21.48413, "lng": 86.7912729}], "Kailash Choudhary": ["Barmer, Rajasthan 344001, India", {"lat": 25.7521467, "lng": 71.3966865}], "Debasree Chaudhuri": ["Balurghat, West Bengal, India", {"lat": 25.2372834, "lng": 88.7830612}]}
data=mos
'''data=ParseTable()
print(data,len(data))
'''
jsonData={}
for i in data:
	print(i)
	try:
		data1=WikiData("https://en.wikipedia.org"+data[i])
		jsonData[i]=LonLat(data1["Born"])
	except Exception:
		address=input("enter Adress for "+i+":     ")
		if (address=="None"):
			jsonData[i]=None
			continue	
		jsonData[i]=LonLat(address)
print(json.dumps(jsonData))
#"":["",{"lat":,"lng":}]