import re
import pdfScraper  # Local File


def emailExtract(pdf_Scrape):
    """Extracts Email ID's from PDF

    Arguments:
        pdf_Scrape {list} -- List containing information of each page as list elements
    """
    for i in pdf_Scrape:
        # Create regex for email id: xyz@abc.com
        email_Rx = re.compile(r'[\w]+@[\w]+\.[\w]{2,3}')
        extract_Email = str(email_Rx.findall(i))

        with open('Email_Data.txt', 'a+') as file_Obj:
            file_Obj.write(extract_Email)

    print("All Email ID's are saved to Email Data.txt")


def phoneExtract(pdf_Scrape):
    """Extracts Phone Numbers from PDF.

    Arguments:
        pdf_Scrape {list} -- List containing information of each page as list elements
    """
    for i in pdf_Scrape:
        # Create regex for phone number: 123-456-7890, (123)-456-7890
        phone_Rx = re.compile(r'(([\d]{3}|\([\d]{3}\))(-|\s)[\d]{3}-[\d]{4})')
        extract_Phone = phone_Rx.findall(i)
        final_Phone = str([x[0] for x in extract_Phone])

        with open('Phone_Data.txt', 'a+') as file_Obj:
            file_Obj.write(final_Phone)

    print("All Phone Numbers are saved to Phone Data.txt")


if __name__ == "__main__":

    pdf_Path = "PhoneDirectory_web.pdf"
    info_List = pdfScraper.extractPDF(pdf_Path)

    emailExtract(info_List)
    phoneExtract(info_List)
