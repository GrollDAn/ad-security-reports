from tabulate import tabulate

# ANSI-коды для цветов
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def parse_sddl(sddl):
    """Разбивает SDDL на список ACE"""
    sddl = sddl.strip()
    ace_list = []
    current = ""
    depth = 0
    for c in sddl:
        if c == '(':
            if depth == 0:
                current = ""
            depth += 1
            current += c
        elif c == ')':
            depth -= 1
            current += c
            if depth == 0:
                ace_list.append(current)
        else:
            current += c
    return ace_list

def extract_header(sddl):
    """Возвращает часть SDDL до первой скобки"""
    idx = sddl.find("(")
    return sddl[:idx] if idx != -1 else sddl

def diff_sddl(sddl1, sddl2):
    list1 = parse_sddl(sddl1)
    list2 = parse_sddl(sddl2)

    set1 = set(list1)
    set2 = set(list2)

    all_aces = sorted(set1 | set2)  # все уникальные ACE, объединение

    table = []

    # --- Метаданные (шапка) ---
    header1 = extract_header(sddl1)
    header2 = extract_header(sddl2)

    if header1 != header2:
        if header1 and not header2:
            header1 = f"{RED}{header1}{RESET}"
        elif header2 and not header1:
            header2 = f"{GREEN}{header2}{RESET}"
        else:  # оба есть, но разные
            header1 = f"{RED}{header1}{RESET}"
            header2 = f"{GREEN}{header2}{RESET}"

    table.append([header1, header2])

    # --- ACE ---
    for ace in all_aces:
        left = ace if ace in set1 else ""
        right = ace if ace in set2 else ""

        if left and not right:
            left = f"{RED}{left}{RESET}"
        if right and not left:
            right = f"{GREEN}{right}{RESET}"

        table.append([left, right])

    return table

if __name__ == "__main__":
    with open("sddl_RSAT.txt") as f:
        sddl1 = f.read()
    with open("sddl_ADMC.txt") as f:
        sddl2 = f.read()

    table = diff_sddl(sddl1, sddl2)

    print(tabulate(table, headers=["RSAT", "ADMC"], tablefmt="github"))
