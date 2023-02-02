from pathlib import Path
import overheads,cash_on_hand,profit_loss

def main():
    overheads_output = overheads.highest_overheads()
    file_path = Path.cwd()/"summary_report.txt"
    with file_path.open(mode="a", encoding="UTF-8") as file:
        file.writelines(overheads_output)

    coh_output = cash_on_hand.cash_difference()
    file_path = Path.cwd()/"summary_report.txt"
    with file_path.open(mode="a", encoding="UTF-8") as file:
        file.writelines(coh_output)

    np_output = profit_loss.net_profit()
    file_path = Path.cwd()/"summary_report.txt"
    with file_path.open(mode="a", encoding="UTF-8") as file:
        file.writelines(np_output)

            