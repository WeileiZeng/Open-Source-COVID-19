# use python3
# render csv to markdown
# note: the markdown for github is a little bit hard to render. The table must have an extra blank line in front of it and right after it. Also, Chinese blanket ( ) is also not supported in the table


import pytablereader as ptr
import pytablewriter as ptw
from pytablewriter import HtmlTableWriter
from pytablewriter import MarkdownTableWriter

def soft_wrap(text, width):
    #not finish
    #wrap a long text to given width
    length=len(text)
    interval=int(length/width)
    for i in range(interval):
        text= text[0:pos]+' '
        
    

def convert(csv_file_path, html_file_path,table_name):
    print("this python script read table in ",csv_file_path, " and then write it into html file ",html_file_path)
    print("converting...")
    #writer = HtmlTableWriter()
    writer = MarkdownTableWriter()
    #writer.is_write_header=False
    writer.from_csv(csv_file_path)
    writer.table_name = table_name


    #get the column for link
    link_col=0
    for head in writer.headers:
        #print(head)
        if ( head == '链接' ):
            break
        else:
            link_col +=1
    #debug
    link_col_flag = True
    if ( link_col >= len(writer.headers) ):
        link_col_flag = False
        #raise ValueError('no column for link')
    
    print('get link_col = ',link_col)

    #get the column for wuzi
    wuzi_col=0
    for head in writer.headers:
        #print(head)
        if ( head == '物资' ):
            break
        else:
            wuzi_col +=1
    #debug
    wuzi_col_flag = True
    if ( wuzi_col >= len(writer.headers) ):
        wuzi_col_flag = False
        #raise ValueError('no column for wuzi')
    
    print('get wuzi_col = ',wuzi_col)

    
    #limit width of some column to be
    col_fixed_width=wuzi_col
    col_width=24
    #modify the link in the fourth row to be an html link
    
    for row in writer.value_matrix:
        if wuzi_col_flag and len(row[col_fixed_width]) > col_width :
            row[col_fixed_width]=row[col_fixed_width][0:col_width]
        #row[3]='\n <a href="'+row[3]+'"> link </a> \n'
        if link_col_flag and ( row[link_col] != '' ):
            row[link_col]='[link]('+row[link_col]+')'
    writer.dump(html_file_path)
    print("done with ",table_name)

def main():
    #convert all csv to markdown
    data_path=""
    build_path="./_includes/"
    #build_path="./../page/"
    
    csv_file_path = "repo-collection.csv"
    html_file_path = "repo-collection.md"
    table_name = '' 
    convert(data_path + csv_file_path, build_path + html_file_path,table_name)


if __name__=="__main__":
    main()

