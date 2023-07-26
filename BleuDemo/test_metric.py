from Sacrebleu import Sacrebleu
import pandas as pd

# predictions = [
#     """
#         let pro:ProductCatalog in
#         pro.oclIsNew() and
#         pro.Id = id and
#         pro.Name = name and
#         ProductCatalog.allInstance()->includes(pro) and
#         result = true
#     """
#     "hello there general kenobi", "foo bar foobar"
# ]
# references = [
#     [
#         """
#        let pro:ProductCatalog in
#        pro.oclIsNew() and
#        pro.Id = id and
#        pro.Name = name and
#        ProductCatalog.allInstance()->includes(pro) and
#        result = true
#         """
#     ]
# ]
predictions = []
references = []


def excel_one_line_to_list():
    # predictions_ex = pd.read_excel(io=r'D:\workplace\BLEU Demo\BLEU选取数据集.xlsx', usecols=[1],
    #                                names=None)
    # references_ex = pd.read_excel(io=r'D:\workplace\BLEU Demo\BLEU选取数据集.xlsx', usecols=[2],
    #                               names=None)
    predictions_ex = pd.read_excel(io=r'.\BLEU选取数据集.xlsx', usecols=[1],
                                   names=None)
    references_ex = pd.read_excel(io=r'.\BLEU选取数据集.xlsx', usecols=[2],
                                  names=None)
    predictions_ex_li = predictions_ex.values.tolist()
    references_ex_li = references_ex.values.tolist()
    for s_li in predictions_ex_li:
        predictions.append(s_li[0])
    for r_li in references_ex_li:
        references.append(r_li)
    # print(predictions)
    # print(references)


# predictions = ["hello there general kenobi", "foo bar foobar"]
# references = [['hello there general kenobi', 'hello there !'], ['foo bar foobar', 'foo bar foobar']]

if __name__ == '__main__':
    excel_one_line_to_list()
    bleu = Sacrebleu()
    b = bleu.compute(predictions=predictions, references=references)
    print(b)
