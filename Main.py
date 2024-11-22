import random
import re
import AnsRes as res
def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)


    response(res.res_es[0],res.res_es[1],res.res_es[2],res.res_es[3])
    response(res.res_hola[0], res.res_hola[1], res.res_hola[2])
    response(res.res_ub[0], res.res_ub[1], res.res_ub[2])
    response(res.res_hor[0], res.res_hor[1], res.res_hor[2])
    response(res.res_ins[0], res.res_ins[1], res.res_ins[2],res.res_ins[3])
    response(res.reb_bec[0], res.reb_bec[1], res.reb_bec[2])
    response(res.res_tran[0], res.res_tran[1], res.res_tran[2])
    response(res.res_orb[0], res.res_orb[1], res.res_orb[2])
    response(res.res_doc[0], res.res_doc[1], res.res_doc[2])
    response(res.res_record[0], res.res_record[1], res.res_record[2])
    response(res.res_th[0], res.res_th[1], res.res_th[2])

    best_match = max(highest_prob, key=highest_prob.get)
    # print(highest_prob)

    return unknown() if highest_prob[best_match] < 1 else best_match


def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][
        random.randrange(3)]
    return response


while True:
    print("Bot: " + get_response(input('You: ')))