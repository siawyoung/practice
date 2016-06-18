# Given a current absolute path, e.g., "/usr/bin/mail", and a relative one, e.g, "../../../etc/xyz/../abc" return the absolute path created from the combination of the first two paths. In the example strings, the answer should be "/etc/abc".


def get_path(abs_path, relative_path):
    curr_path = abs_path.split('/')[1:]

    relative_path = relative_path.split('/')
    print(relative_path)
    for i in relative_path:

        if i == '..':
            curr_path.pop()
        else:
            curr_path.append(i)
        print(curr_path)



    return  '/' + '/'.join(curr_path)

print(get_path('/usr/bin/mail', '../../../etc/xyz/../abc'))

