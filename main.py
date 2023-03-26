# Project: QAP 4, One Stop Insurance Company
# Written by: Josh White
# Date: March 20

import datetime




# Read the default files from OSICDef.dat

f = open('OSICDef.dat', 'r')

policy_num = int(f.readline())
basic_prem = float(f.readline())
add_car_disc = float(f.readline())
ext_li_cov = float(f.readline())
glass_cov = float(f.readline())
loan_cov = float(f.readline())
HST_rate = float(f.readline())
mon_proc_fee = float(f.readline())

f.close()

# USER INPUTS
while True:
    first_name = input("Please enter your first name: ").title()
    last_name = input("Please enter your last name: ").title()
    address = input("Please enter your street address: ").title()
    prov_list = ["NL", "NS", "NB", "PE", "QC", "ON", "SK", "MB", "AB", "BC"]

    while True:
        prov = input("Please enter your province (XX): ").upper()
        if not prov in prov_list:
            print("Not a valid entry, please try again ")
        else:
            break

    while True:
        postal_code = input("Please enter your postal code(X0X0X0): ").upper()
        if len(postal_code) != 6:
            print("Not a valid entry, please try again")
        else:
            break

    while True:
        phone_num = input("Please enter your phone number (XXXXXXXXXX): ")
        if len(phone_num) != 10:
            print("Not a valid entry, please try again")
        elif not (phone_num).isdigit:
            print("Not a valid entry, please try again")
        else:
            break

    num_cars = int(input("Please enter the number of cars your are looking to insure: "))

    while True:
        extra_liab = input("Would you like to add extra liability for up to $1000.00 (Y/N) ").upper()
        if extra_liab != "Y" and extra_liab != "N":
            print("Not a valid entry, please try again")
        else:
            break

    while True:
        glass = input("Would you like to add additional glass coverage (Y/N) ").upper()
        if glass != "Y" and glass != "N":
            print("Not a valid entry, please try again")
        else:
            break

    while True:
        loaner = input("Would you like a loaner car (Y/N) ").upper()
        if loaner != "Y" and loaner != "N":
            print("Not a valid entry, please try again")
        else:
            break

    while True:
        payment = input("Would you like to pay in full or monthly payments (F/M) ").upper()
        if payment != "F" and payment != "M":
            print("Not a valid entry, please try again")
        else:
            break

    tdelta = datetime.timedelta(days=30)

    # CALCULATIONS
    add_car = int(num_cars - 1)
    inv_disc_price = basic_prem * add_car_disc
    disc_price = basic_prem - inv_disc_price
    add_car_cov = add_car * disc_price

    print(add_car_cov)

    if extra_liab == "Y":
        extra_liabx = ext_li_cov
    else:
        extra_liabx = 0

    if glass == "Y":
        glassx = glass_cov
    else:
        glassx = 0

    if loaner == "Y":
        loanerx = loan_cov
    else:
        loanerx = 0

    extra_costs = loanerx + glassx + extra_liabx + add_car_cov

    subtotal = extra_costs + basic_prem

    HST = subtotal * HST_rate
    total_cost = subtotal + HST

    if payment == "M":
        monthly_payment = (total_cost + 39.99) / 8
    else:
        monthly_payment = 0
    inv_date = datetime.date.today()
    payment_date = inv_date + tdelta

    #FORMATTING FOR OUTPUTS
    inv_date = datetime.datetime.strftime(inv_date, '%d %b,%Y')
    payment_date= datetime.datetime.strftime(payment_date,'%d %b,%Y')
    basic_prem_DSP = "${:,.2f}".format(basic_prem)
    add_car_cov_dsp = "${:,.2f}".format(add_car_cov)
    extra_liab_DSP = "${:,.2f}".format(extra_liabx)
    glass_cov_DSP = "${:,.2f}".format(glassx)
    loaner_DSP = "${:,.2f}".format(loanerx)
    extra_costs_dsp = "${:,.2f}".format(extra_costs)
    subtotal_dsp = "${:,.2f}".format(subtotal)
    HST_DSP = "${:,.2f}".format(HST)
    total_cost_dsp = "${:,.2f}".format(total_cost)
    if payment == "M":
        monthly_payment_dsp = "MONTHLY PAYMENTS:                ${:,.2f}".format(monthly_payment)
    else:
        monthly_payment_dsp = ""

    if payment == "M":
        pay_date_DSP = f"FIRST PAYMENT DATE:          {payment_date}"
    else:
        pay_date_DSP = ""


    #DISPLAY OUTPUT
    print()
    print("        ==============================")
    print("        --- ONE STOP INSURANCE CO. ---")
    print("        ==============================")
    print(f"        NAME:    {first_name} {last_name} ")
    print(f"        ADDRESS: {address}")
    print(f"                 {prov}")
    print(f"                 {postal_code}")
    print(f"        PHONE:   {phone_num}")
    print("----------------------------------------------")
    print(f"DATE: {inv_date:<13}            POLICY NO: {policy_num:>4}")
    print(f"NUMBER OF VEHICLES ON CLAIM:{num_cars:>2}")
    print(f"      BASIC PREMIUM:                {basic_prem_DSP:>10}")
    print(f"      ADDITIONAL VEHICLES:          {add_car_cov_dsp:>10}")
    print(f"      EXTRA LIABILITY:              {extra_liab_DSP:>10}")
    print(f"      GLASS COVERAGE:               {glass_cov_DSP:>10}")
    print(f"      LOANER CAR:                   {loaner_DSP:>10}")
    print("      ----------------------------------------")
    print(f"      SUBTOTAL:                     {subtotal_dsp:>10}")
    print(f"      HST:                          {HST_DSP:>10}")
    print("      ----------------------------------------")
    print(f"      TOTAL:                        {total_cost_dsp:>10}")
    print("      ========================================")
    print(f"      {monthly_payment_dsp}")
    print(f"      {pay_date_DSP}")



    #DAVE THE DATA FILE TO POLICIES.DAT

    f = open("Policies.dat", "a")
    f.write("{}, ".format(str(policy_num)))
    f.write("{}, ".format(str(inv_date)))
    f.write("{}, ".format(str(first_name)))
    f.write("{}, ".format(str(last_name)))
    f.write("{}, ".format(str(address)))
    f.write("{}, ".format(str(prov)))
    f.write("{}, ".format(str(postal_code)))
    f.write("{}, ".format(str(phone_num)))
    f.write("{}, ".format(str(postal_code)))
    f.write("{}, ".format(str(num_cars)))
    f.write("{}, ".format(str(extra_liab)))
    f.write("{}, ".format(str(glass)))
    f.write("{}, ".format(str(loaner)))
    f.write("{}, ".format(str(payment)))
    f.write("{}\n ".format(str(total_cost)))

    f.close()
    print()
    print('Policy information processed and saved.')

    policy_num += 1

    Continue = input("Would you like to process another claim?(Y/N): ").upper()
    if Continue != "Y":
        break

f = open('OSICDef.dat', 'w')
f.write("{}\n ".format(policy_num))
f.write("{}\n ".format(basic_prem))
f.write("{}\n ".format(add_car_disc))
f.write("{}\n ".format(ext_li_cov))
f.write("{}\n ".format(glass_cov))
f.write("{}\n ".format(loan_cov))
f.write("{}\n ".format(HST_rate))
f.write("{}\n ".format(mon_proc_fee))

f.close()

