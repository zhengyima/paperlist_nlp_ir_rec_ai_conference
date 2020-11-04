# paperlist_nlp_ir_recsys_ai_conference
2016-至今 NLP/IR/RecSys/AI领域的相关顶会论文清单paperlist列表含目录，方便直接搜索关键字。

涵盖的conferences包括AAAI/ACL/EMNLP/IJCAI/SIGIR/CIKM/WSDM/WWW/NIPS/COLING/KDD/ICLR。

会议列表可在```papers_index.txt```文件中查看。

## How To Use
直接使用Sublime/VSCode，在```papers.txt```中使用ctrl+F搜索关键字查找论文。然后去Google论文标题，下载之。

每个论文对应的会议，可查看```papers_index.txt```文件，里面记录了每个会议在```papers.txt```的开始行数和结束行数。（其实不需要这一步，直接去Google论文标题一般也能看到所在会议）

可使用```find.py```进行简单的搜索功能，如搜索包含```memory```和```generation```的论文。

```python find.py --q memory_generation```

## Tips
这是方便自己搜索文献的项目。动机是因为acm和dblp搜索结果太乱，而且都无法完全覆盖以上会议（比如acm和dblp都搜不到acl）。

之后可能会考虑更加友好的搜索方式。
