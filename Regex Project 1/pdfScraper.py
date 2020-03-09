import PyPDF2


def extractPDF(path):
    """Extracts Page-Wise Information from PDF.

    Arguments:
        path {String} -- Path to PDF file

    Returns:
        {list} -- List containing information of each page as list elements
    """
    page_Data = []

    with open(path, 'rb') as read_Obj:
        reader = PyPDF2.PdfFileReader(read_Obj)
        tot_Page = reader.getNumPages()

        for i in range(tot_Page):
            page_Obj = reader.getPage(i)
            page_Data.append(page_Obj.extractText())
            """
            Individual Info pieces
            doc_Info = reader.getDocumentInfo(read_Obj)
            f'''
                Information about {pdf_path}:

                Author: {information.author}
                Creator: {information.creator}
                Producer: {information.producer}
                Subject: {information.subject}
                Title: {information.title}
                Number of pages: {number_of_pages}'''
            """

    return page_Data
