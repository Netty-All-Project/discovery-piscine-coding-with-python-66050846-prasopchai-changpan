import sys
#sys เป็นการรับค่าผ่าน command line arguments
def count_parameters():
    num_params = len(sys.argv) - 1 # ลบ 1 เพราะ sys.argv[0] คือชื่อไฟล์ .py
    print(f"Number of parameters: {num_params}.")

count_parameters()