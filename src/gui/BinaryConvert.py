import tkinter as tk
import tkinter.messagebox
import sys

def decimal_to_binary(value):
    return bin(int(value))
def decimal_to_hex(value):
    return hex(int(value))
def binary_to_hex(value):
    return hex(int(value, 2))
def binary_to_decimal(value):
    return int(value, 2)
def hex_to_binary(value):
    return bin(int(value, 16))
def hex_to_decimal(value):
    return int(value, 16)

class BinaryConvert():
    C_FONT = ("Consolas", 16)
    C_TXT_MAXLEN = 32
    
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Pwnable - Binary Converter")
        self.master.geometry("800x480")
        self.num_label = tk.Label(self.master, text="Number:", font=self.C_FONT)
        self.num_label.place(x=200,y=20)

        self.text_input = tk.Entry(self.master, width=20, font=self.C_FONT)
        self.text_input.place(x=300,y=20)

        self.Binary_button = tk.Button(
            self.master, text="Binary", width=7, command=self.evt_bt_bin, font=self.C_FONT)
        self.Binary_button.place(x=250,y=60)

        self.Decimal_button = tk.Button(
            self.master, text="Decimal",width=7, command=self.evt_bt_dec, font=self.C_FONT)
        self.Decimal_button.place(x=355,y=60)

        self.Hex_button = tk.Button(self.master, text="Hex", width=7, command=self.evt_bt_hex, font=self.C_FONT)
        self.Hex_button.place(x=460,y=60)

        self.bin_label = tk.Label(self.master, text="Binary:", font=self.C_FONT)
        self.bin_label.place(x=200,y=125)

        self._stringvar_bin = tk.StringVar()

        self.bin_output = tk.Entry(
            self.master, textvariable=self._stringvar_bin, state="readonly", font=self.C_FONT)
        self.bin_output.place(x=300,y=125)

        self.dec_label = tk.Label(self.master, text="Decimal:", font=self.C_FONT)
        self.dec_label.place(x=200,y=175)

        self._stringvar_dec = tk.StringVar()

        self.dec_output = tk.Entry(
            self.master, textvariable=self._stringvar_dec, state="readonly", font=self.C_FONT)
        self.dec_output.place(x=300,y=175)

        self.hex_label = tk.Label(self.master, text="Hex:", font=self.C_FONT)
        self.hex_label.place(x=200,y=225)

        self._stringvar_hex = tk.StringVar()

        self.hex_output = tk.Entry(
            self.master, textvariable=self._stringvar_hex, state="readonly", font=self.C_FONT)
        self.hex_output.place(x=300,y=225)


    def evt_bt_bin(self):
        try:
            bin_value = self.text_input.get().strip().replace(" ", "")
            dec_value = binary_to_decimal(bin_value)
            hex_value = binary_to_hex(bin_value)

            self._set_values(bin_value, dec_value, hex_value)

        except Exception as ex:
            tk.messagebox.showerror("Error", "Invalid conversion")
            print(ex, file=sys.stderr)

    def evt_bt_dec(self):
        try:
            dec_value = self.text_input.get().strip().replace(" ", "")
            bin_value = decimal_to_binary(dec_value)
            hex_value = decimal_to_hex(dec_value)
            
            self._set_values(bin_value, dec_value, hex_value)
            
        except Exception as ex:
            tk.messagebox.showerror("Error", "Invalid conversion")
            print(ex, file=sys.stderr)

    def evt_bt_hex(self):
        try:
            hex_value = self.text_input.get().strip().replace(" ", "")
            bin_value = hex_to_binary(hex_value)
            dec_value = hex_to_decimal(hex_value)
            
            self._set_values(bin_value, dec_value, hex_value)

        except Exception as ex:
            tk.messagebox.showerror("Error", "Invalid conversion")
            print(ex, file=sys.stderr)

    def _set_values(self, bin_value, dec_value, hex_value):
        if not bin_value.startswith("0b"):
            self.bin_value = "0b" + bin_value
        if not hex_value.startswith("0x"):
            self.hex_value = "0x" + hex_value

        self._stringvar_bin.set(bin_value)
        self._stringvar_dec.set(dec_value)
        self._stringvar_hex.set(hex_value)

    def mainloop(self):
        self.master.mainloop()

# if __name__ == "__main__":
#     # root = tk.Tk()
#     root = BinaryConvert()
#     root.mainloop()
