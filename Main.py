# -*- coding: utf-8 -*-
from Spider import Spider, COLLECTION_SCI
from PaperExcel import PaperExcel


if __name__=="__main__":
    paper_title_list = PaperExcel.read_title_list('./test.xlsx')
    paper_excel_writer = PaperExcel('./result.xlsx')
    FIT3_524_spider = Spider()
    FIT3_524_spider.enable_collection(COLLECTION_SCI)
    for paper_title in paper_title_list:
        paper, error = FIT3_524_spider.search_paper(paper_title)
        if not error == 'no error':
            # 开文件记录错误列表
            print(error)
            continue
        print('Successfully get paper:')
        print(paper)
        cite_papers, cite_url, error = FIT3_524_spider.search_cite_papers(paper, COLLECTION_SCI)
        if not error == 'no error':
            # 开文件记录错误列表
            print(error)
            continue
        print('Cited paper count: %d'% len(cite_papers))
        paper_excel_writer.write_paper_cite(paper, cite_papers)
