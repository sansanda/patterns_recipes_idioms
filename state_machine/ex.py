tabla = {
    ('hola','a'):('aa','ab','ac'),
    ('hola','b'):('ba','bb','bc')
         }
print(tabla['hola','b'])

# {(CurrentState, InputA) : (ConditionA, TransitionA, NextA),
#  (CurrentState, InputB) : (ConditionB, TransitionB, NextB),
#  (CurrentState, InputC) : (ConditionC, TransitionC, NextC),
#  ...
# }

#Cuando dado un estado llega una entrada válida se debe cumplir una Condition para cambiar al estado correspondiente, ejemplo:
#   Dada uma maquina dispensadora se encuentra en el estado inicial (preparada) y hay un inputA ()

def nextState (input):


    table_keys = tabla.keys() #every key is a pair state, input
    for key in table_keys:
        if input

    # while (it.hasNext()):
    #     Object[] tran = (Object[])it.next()
    #     if input == tran[0] or input.getClass() == tran[0]:
    #         if tran[1] != null:
    #             Condition
    #             c = (Condition)
    #             tran[1]
    #             if (!c.condition(input))
    #             continue  # Failed test
    #
    #     if (tran[2] != null)
    #         ((Transition)tran[2]).transition(input)
    #     state = (State)tran[3]
    #     return

nextState('a')