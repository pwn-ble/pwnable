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
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Pwnable - Binary Converter")
        self.master.geometry("800x480")

        self.label = tk.Label(self.master, text="Number:")
        self.label.pack()

        self.text_input = tk.Entry(self.master, width=10)
        self.text_input.pack()

        self.Binary_button = tk.Button(
            self.master, text="Binary", width=6, command=self.evt_bt_bin)
        self.Binary_button.pack()

        self.Decimal_button = tk.Button(
            self.master, text="Decimal",width=6, command=self.evt_bt_dec)
        self.Decimal_button.pack()

        self.Hex_button = tk.Button(self.master, text="Hex", width=6, command=self.evt_bt_hex)
        self.Hex_button.pack()

        self.label = tk.Label(self.master, text="Binary:")
        self.label.pack()

        self._stringvar_bin = tk.StringVar()

        self.output = tk.Entry(
            self.master, textvariable=self._stringvar_bin, state="readonly")
        self.output.pack()

        self.label = tk.Label(self.master, text="Decimal:")
        self.label.pack()

        self._stringvar_dec = tk.StringVar()

        self.output = tk.Entry(
            self.master, textvariable=self._stringvar_dec, state="readonly")
        self.output.pack()

        self.label = tk.Label(self.master, text="Hex:")
        self.label.pack()

        self._stringvar_hex = tk.StringVar()

        self.output = tk.Entry(
            self.master, textvariable=self._stringvar_hex, state="readonly")
        self.output.pack()


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
if __name__ == "__main__":
    # root = tk.Tk()
    root = BinaryConvert()
    root.mainloop()
