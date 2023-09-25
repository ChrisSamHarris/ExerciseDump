import pandas as pd
from fpdf import FPDF

file_loc = "articles.csv"
df = pd.read_csv(file_loc, dtype={"id": str})
# Ensure we check the type of data interpreted = print(df.dtypes)
receipt_df = pd.read_csv("receipt_num.csv")

print(df)


class ArticlePurchase:
    def __init__(self, article_id):
        self.id = article_id
        self.stock = df.loc[df["id"] == self.id, "in_stock"].squeeze()
        self.name = df.loc[df["id"] == self.id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.id, "price"].squeeze()
        
    def in_stock(self):
        if self.stock > 0:
            return True
        else:
            return False
        
    def generate_receipt(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{receipt_df}", ln=1)
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.name.title()}", ln=1)
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.price}", ln=1)

        pdf.output("receipt.pdf")
        
    def adjust_data(self):
        """Book a hotel by changing its availability to a no"""
        df.loc[df["id"] == self.id, "in_stock"] -= 1
        df.to_csv(file_loc, index=False)
        
        receipt_df["receipt_num"] += 1
        receipt_df.to_csv("receipt_num.csv", index=False)
        

article_ID = input("Choose an article to buy (ID): ")
article_purchase = ArticlePurchase(article_id=article_ID)

if article_purchase.in_stock():
    article_purchase.generate_receipt()
    article_purchase.adjust_data()
    print("Receipt has been generated!")
else:
    print("This item is currently out of stock!")