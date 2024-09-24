import random

# تعريف مجموعة أوراق اللعب
cards = [
    '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'
] * 4  # تحتوي على 4 مجموعات

# خلط الأوراق
random.shuffle(cards)

# دالة لتوزيع البطاقات
def deal_cards(cards, num_of_cards):
    return [cards.pop() for _ in range(num_of_cards)]

# تحديد قيمة الورقة
def card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

# دالة لعرض البطاقات
def display_hand(hand):
    return ", ".join(hand)

# دالة التحقق من الانتصار (عند جمع قيمة الأوراق 11)
def check_win(player_total, dealer_total):
    if player_total == 11:
        return "اللاعب فاز بجمع 11!"
    elif dealer_total == 11:
        return "الموزع فاز بجمع 11!"
    return None

# البدء في اللعبة
def play_game():
    print("مرحبًا بكم في لعبة الباصرة!")
    
    # توزيع 4 بطاقات لكل لاعب
    player_hand = deal_cards(cards, 4)
    dealer_hand = deal_cards(cards, 4)
    table_cards = deal_cards(cards, 4)  # بطاقات موجودة على الطاولة
    
    player_total = 0
    dealer_total = 0
    
    print(f"بطاقات الطاولة: {display_hand(table_cards)}")
    
    # دور اللاعب والموزع بالتناوب
    while True:
        # دور اللاعب
        print(f"\nبطاقات اللاعب: {display_hand(player_hand)}")
        try:
            player_choice = int(input(f"اختر ورقة من يدك (1-{len(player_hand)}): ")) - 1
            chosen_card = player_hand.pop(player_choice)
            player_total += card_value(chosen_card)
            print(f"أنت لعبت: {chosen_card} - المجموع الحالي: {player_total}")
        except (ValueError, IndexError):
            print("اختيار غير صالح. حاول مرة أخرى.")
            continue
        
        # تحقق من الانتصار
        result = check_win(player_total, dealer_total)
        if result:
            print(result)
            break

        # دور الموزع (اختيار ورقة عشوائية)
        dealer_choice = random.choice(dealer_hand)
        dealer_hand.remove(dealer_choice)
        dealer_total += card_value(dealer_choice)
        print(f"\nالموزع لعب: {dealer_choice} - المجموع الحالي للموزع: {dealer_total}")
        
        # تحقق من الانتصار
        result = check_win(player_total, dealer_total)
        if result:
            print(result)
            break

        # إنهاء اللعبة إذا انتهت البطاقات
        if not player_hand and not dealer_hand:
            print("\nانتهت البطاقات!")
            if player_total > dealer_total:
                print("اللاعب فاز!")
            elif dealer_total > player_total:
                print("الموزع فاز!")
            else:
                print("تعادل!")
            break

if __name__ == "__main__":
    play_game()
