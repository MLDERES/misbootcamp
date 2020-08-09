from challenge_tests import assert_equal

def day_of_year(day, month, year):
    ''' A function to determine what day of the year it is
    Parameters
    ----------
    day : int
        The day of the month
    month : int
        The month of the year
    year : int
        The year which the day is being calculated
    '''
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = day
    for m in range(month -1):
        total_days = total_days+days_in_month[m]
    if (month > 2) and is_leap_year(year):
        total_days = total_days + 1
        
    return total_days

def is_leap_year(y):
    return (y % 4 == 0) and ((y % 100 != 0) or (y % 400 == 0))

def relations(family_tree, relationship):
    ''' Determine the relationship between two people in a given family
    
    Parameters
    ----------
    family_tree : list of tuple of str
        The family tree is defined by tuples of mother/daughter pairs 
        where the first item in the tuple is the mother of the second name in the tuple.
    relationship: tuple of str
        The relationship to be determined of the second person in the tuple to the first person in the tuple
        
    Returns
    -------
    str : {'Grandmother','Granddaughter','Mother','Daughter','Sister','Cousin','Aunt','Niece'}
        The relationship of the second person in the `relationship` tuple to the first person in the tuple
        
    '''
    # Replace pass with your code
    parents = {}
    for parent, child in family_tree:
        # Build a list of children by specifying the parent
        parents[child]  = parent
        
    # Now get the targets
    gen_1 = relationship[0]
    gen_2 = relationship[1]
    
    gen_1_parent = parents.get(gen_1)
    gen_1_parent_parent = parents.get(gen_1_parent)
    gen_2_parent = parents.get(gen_2)
    gen_2_parent_parent = parents.get(gen_2_parent)
    
    if gen_2 == gen_1_parent : return 'Mother'
    if gen_2 == gen_1_parent_parent : return 'Grandmother'
    if gen_1 == gen_2_parent : return 'Daughter'
    if gen_1 == gen_2_parent_parent : return 'Granddaughter'
    if gen_1_parent == gen_2_parent : return 'Sister'
    if gen_1_parent_parent == gen_2_parent_parent : return 'Cousin'
    if gen_1_parent_parent == gen_2_parent : return 'Aunt'
    if gen_1_parent == gen_2_parent_parent : return 'Niece'

    

def monogram(full_name):
    '''
    Creates a traditional monogram from a supplied full name
    '''
    first, middle, last = full_name.split(' ',2)
    return f'{first[0].lower()}.{last[0].upper()}.{middle[0].lower()}'


def dispense_cash(amount):
    ''' Determine the minimum number of ATM bills to meet the requested amount to dispense
    
    Parameters
    ----------
    amount : int
        The amount of money requested from the ATM
        
    Returns
    -------
    int
        The number of bills needed, -1 if it can't be done
    '''
    total_bills = 0
    if amount % 10 != 0:
        return -1 # Can't be done, because it has to be a multiple of 10
    
    b_500 = (amount // 500) # The // operator does integer only division - such that 4 // 3 = 1
    b_100 = (amount % 500) // 100
    b_50 = (amount - (b_500*500) - (b_100 *100)) // 50
    b_20 = (amount - (b_500*500) - (b_100 *100) - (b_50 * 50)) // 20
    b_10 = (amount - (b_500*500) - (b_100 *100) - (b_50 * 50) - (b_20 * 20)) // 10
    
    total_bills = b_500 + b_100 + b_50 + b_20 + b_10
    return total_bills



def test_monogram():
    # Basic tests
    assert_equal(monogram('Dwight Kevin Shrute'),'d.S.k')
    assert_equal(monogram('Eye see deadpeople'),'e.D.s', hint='Did you check the case?')
    assert_equal(monogram('mers sadees benz II'),'m.B.s',hint='Did the extra suffix throw you off?')


def test_atm():
    assert_equal(dispense_cash(1120), 4)
    assert_equal(dispense_cash(492), -1)
    assert_equal(dispense_cash(440), 6)
    assert_equal(dispense_cash(370), 5)
    assert_equal(dispense_cash(80), 3)

def test_family_tree():
    # Run this cell to test your work
    family_a = [("Enid", "Susan"), ("Susan", "Deborah")]
    family_b = [('Enid', 'Susan'), ('Susan', 'Deborah'), ('Enid', 'Dianne'), ('Dianne', 'Judy'), ('Dianne', 'Fern')]

    '''
    Enid
    |
    Susan       Dianne
      |             |           |
    Deborah     Judy        Fern
    '''

    assert_equal(relations(family_a,('Enid','Susan')),'Daughter')
    assert_equal(relations(family_b,('Enid','Judy')),'Granddaughter')
    assert_equal(relations(family_b,('Enid','Deborah')),'Granddaughter')
    assert_equal(relations(family_b,('Enid','Dianne')),'Daughter')
    assert_equal(relations(family_b,('Enid','Fern')),'Granddaughter')
    assert_equal(relations(family_b,('Susan','Enid')),'Mother')
    assert_equal(relations(family_b,('Susan','Deborah')),'Daughter')
    assert_equal(relations(family_b,('Susan','Dianne')),'Sister')
    assert_equal(relations(family_b,('Susan','Judy')),'Niece')
    assert_equal(relations(family_b,('Susan','Fern')),'Niece')
    assert_equal(relations(family_b,('Fern','Susan')),'Aunt')
    assert_equal(relations(family_b,('Fern','Judy')),'Sister')
      

def test_day_of_year():
    assert_equal(day_of_year(1,1,2000),1,'Jan 1, 2000')
    assert_equal(day_of_year(15,2,2015),46,'Feb 2, 2015')
    assert_equal(day_of_year(30,6,2020),182,'June 30, 2020', 'Did you check for leap year?')


def fruit_calculator(question):
    # Set the quantity to zero
    # For each word in the string
    #   If the word is 'loses', then we are going to be subtracting
    #   If the word is a number, then convert it to an integer, if the 
    #   If the previous word was a number (the value of number is not zero),
    #      then add this word to a dictionary as a key and add the number to the value
    # Find the last word, remove the '?' and look it up in dictionary - this is the value
    
    # Set the qty to zero
    qty = 0 
    lose = False
    fruits = {}
    words = question.split(' ')
    # For each word in the string
    for w in words:
        
        # Since the split may include `.` or `,` we need to take these off
        w = w.rstrip('.').rstrip(',')
        if w == 'loses':
            lose = True
        
        #   If the word is a number, then figure out if this is a gain, loss or just has
        if w.isdigit():
            qty = int(w)
            # Gains and Loses is 0 if there hasn't been a gain or loss
            if lose:
                qty = qty * -1
                # Need to reset the lose value to False
                lose = False
    
        else:
            #   If the previous word was a number (the value of qty is not zero),
            #      then add this word to a dictionary as a key and add the number to the value
            if qty != 0:
                fruits[w] = fruits.get(w,0) + qty
                qty = 0
    
    # Find the last word, remove the '?' and look it up in dictionary - this is the value
    target_fruit = words[-1].rstrip('?')
    return fruits.get(target_fruit,0)

def test_fruit():
    assert_equal(fruit_calculator('Panda has 8 apples and loses 2 apples.  How many apples?'), 6)
    assert_equal(fruit_calculator('Panda has 8 apples, 2 bananas and gains 3 bananas.  How many bananas?'), 5)
    assert_equal(fruit_calculator('Panda has 8 apples, 2 bananas and gains 3 bananas.  How many apples?'), 8)    
    assert_equal(fruit_calculator('Jim has 12 bananas. He loses 2 apples.  Then he gains 1 apple.  How many bananas?'),12)
    assert_equal(fruit_calculator('Jim has 2 bananas and gains 3 bananas.  How many watermelons?'),0)

if __name__ == "__main__":
    test_day_of_year()
    test_monogram()
    test_family_tree()
    test_atm()
    test_fruit()
    