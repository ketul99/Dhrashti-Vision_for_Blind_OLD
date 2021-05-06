#list of objects to meaningful string
def list_to_string(ans):
    if(len(ans)==1):
        output='There is a '+ans[0]+'.'
    else:
        new_list=[]
        repeated=[]
        for i in ans:
            if i not in new_list:
                new_list.append(i)
            else:
                if i not in repeated:
                    repeated.append(i)

        for i in repeated:
            new_list.remove(i)

        if(new_list==[]):
            output='There are '
        else:
            output='There is '
            
        for i in range(len(repeated)):
            repeated[i]+='s'

        if 'persons' in repeated:
            for i in range(len(repeated)):
                if(repeated[i]=='persons'):
                    repeated[i]='people'

        new_list.extend(repeated)

        if(len(new_list)!=1):
            for i in range(len(new_list)-1):
                output+=new_list[i]+', '
            output+='and '+new_list[-1]+'.'
        else:
            output+=new_list[0]+'.'

    return output