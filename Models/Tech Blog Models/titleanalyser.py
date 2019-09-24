from tkinter import *
import requests
from bs4 import BeautifulSoup
window=Tk()
window.title('Website Title Analyser')
window.geometry('500x500')
text=Label(window,text='Analyse the title of Website',fg='blue',font=('Arial',18))
def titlescrape():
	a=entry_box.get()
	a=str(a)
	page=requests.get(a)
	html=page.content
	soup=BeautifulSoup(html,'html.parser')
	main_title=soup.find('title')
	main_title=main_title.get_text()
	with open('/home/anubhav/Desktop/scraped_title.txt','a') as f:
		f.write(main_title+'\n')
		
		f.close()
	with open('/home/anubhav/Desktop/scraped_title.csv','a') as f:
		f.write(main_title+'\n')
		
		f.close()
text.place(x=60,y=50)
entry_box=Entry(window,text='Please enter the complete url of website to scrape',fg='red',font=('Arial',12))
entry_box.place(x=120,y=200)
button=Button(window,text='Scrape the title of the Website',command=titlescrape,fg='red',font=('Arial',20))
button.place(x=20,y=300)
window.mainloop()