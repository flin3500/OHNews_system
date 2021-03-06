from colorama import Fore, Style
from getpass import getpass
from service.user_service import UserService
from service.news_service import NewsService
from service.role_service import RoleService
from service.type_service import TypeService
import os
import sys
import time

__user_service = UserService()
__news_service = NewsService()
__role_service = RoleService()
__type_service = TypeService()

while True:
    os.system("clear")
    print(Fore.LIGHTBLUE_EX, "\n\t================")
    print(Fore.LIGHTBLUE_EX, "\n\tWelcome to OHNews v0.1")
    print(Fore.LIGHTBLUE_EX, "\n\t================")
    print(Fore.LIGHTGREEN_EX, "\n\t1. Log in")
    print(Fore.LIGHTGREEN_EX, "\n\t2. Exit")
    print(Style.RESET_ALL)
    opt = input("\n\tInput the number: ")
    if opt == "1":
        username = input("\n\tUsername: ")
        password = getpass("\n\tPassword: ")
        result = __user_service.login(username, password)
        # successfully log in
        if result:
            # The user role
            role = __user_service.search_role(username)
            while True:
                os.system("clear")
                if role == "Editor":
                    print(Fore.LIGHTGREEN_EX, "\n\t1. Post news")
                    print(Fore.LIGHTGREEN_EX, "\n\t2. Edit news")
                    print(Fore.LIGHTRED_EX, "\n\t3. Log out")
                    print(Fore.LIGHTRED_EX, "\n\t4. Exit system")
                    print(Style.RESET_ALL)
                    opt = input("\n\tInput the number: ")
                    if opt == "1":
                        os.system("clear")
                        try:
                            title = input("\n\tTitle: ")
                            editor_id = __user_service.search_userid(username)
                            result = __type_service.search_list()
                            for index in range(len(result)):
                                type = result[index]
                                print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, type[1]))
                            print(Style.RESET_ALL)
                            opt = input("\n\tInput the type number: ")
                            type_id = result[int(opt) - 1][0]
                            path_head = os.path.expanduser('~/Desktop/')
                            path = input("\n\tFile path: ")
                            path = path_head + path
                            file = open(path, "r")
                            content = file.read()
                            file.close()
                            if_top = input("\n\tTop level(0-5): ")
                            is_commit = input("\n\tCommit? (y/n): ")
                            if is_commit == "Y" or is_commit == "y":
                                __news_service.add_news(title, editor_id, type_id, content, if_top)
                                print("\n\tAdd Successfully (Wait 1s)")
                                time.sleep(1)
                        except Exception as e:
                            print("\n\tInput invalid (Wait 2s)")
                            time.sleep(2)
                            continue
                    elif opt == "2":
                        page = 1
                        while True:
                            os.system("clear")
                            count_page = __news_service.search_count_page()
                            result = __news_service.search_list(page)
                            for index in range(len(result)):
                                news = result[index]
                                print(Fore.LIGHTBLUE_EX,
                                      "\n\t%d\t%s\t%s\t%s" % (index + 1, news[1], news[2], news[3]))
                            print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                            print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                            print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                            print(Fore.LIGHTRED_EX, "\n\tprev. Prev page")
                            print(Fore.LIGHTRED_EX, "\n\tnext. Next page")
                            print(Fore.LIGHTRED_EX, "\n\tback. Back")
                            print(Style.RESET_ALL)
                            try:
                                opt = input("\n\tInput the number: ")
                                if opt == "prev" and page > 1:
                                    page -= 1
                                elif opt == "next" and page < count_page:
                                    page += 1
                                elif opt == "back":
                                    break
                                elif 1 <= int(opt) <= 5:
                                    os.system("clear")
                                    news_id = result[int(opt) - 1][0]
                                    result = __news_service.search_by_id(news_id)
                                    title = result[0]
                                    type = result[1]
                                    if_top = result[2]
                                    print("\n\tOriginal title: %s" % title)
                                    new_title = input("\n\tNew title: ")
                                    print("\n\tOriginal type: %s" % type)
                                    result = __type_service.search_list()
                                    for index in range(len(result)):
                                        type = result[index]
                                        print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, type[1]))
                                    print(Style.RESET_ALL)
                                    opt = input("\n\tNew type: ")
                                    new_type = result[int(opt) - 1][0]
                                    path_head = os.path.expanduser('~/Desktop/')
                                    path = input("\n\tFile path: ")
                                    path = path_head + path
                                    file = open(path, "r")
                                    content = file.read()
                                    file.close()
                                    print("\n\tOriginal top level: %s" % if_top)
                                    new_if_top = input("\n\tNew top level(0-5): ")
                                    is_commit = input("\n\tCommit? (y/n): ")
                                    if is_commit == "Y" or is_commit == "y":
                                        __news_service.edit_news(news_id, new_title, new_type, content, new_if_top)
                                        print("\n\tEdit Successfully (Wait 1s)")
                                        time.sleep(1)
                            except Exception as e:
                                print("\n\tInput invalid (Wait 2s)")
                                time.sleep(2)
                                continue
                    elif opt == "3":
                        break
                    elif opt == "4":
                        sys.exit(0)
                elif role == "Admin":
                    print(Fore.LIGHTGREEN_EX, "\n\t1. Manage news")
                    print(Fore.LIGHTGREEN_EX, "\n\t2. Manage users")
                    print(Fore.LIGHTRED_EX, "\n\t3. Log out")
                    print(Fore.LIGHTRED_EX, "\n\t4. Exit system")
                    print(Style.RESET_ALL)
                    opt = input("\n\tInput the number: ")
                    if opt == "1":
                        while True:
                            os.system("clear")
                            print(Fore.LIGHTGREEN_EX, "\n\t1. Review news")
                            print(Fore.LIGHTGREEN_EX, "\n\t2. Delete news")
                            print(Fore.LIGHTRED_EX, "\n\t3. Back to account")
                            print(Style.RESET_ALL)
                            opt = input("\n\tInput the number: ")
                            if opt == "1":
                                page = 1
                                while True:
                                    os.system("clear")
                                    count_page = __news_service.search_unreview_count_page()
                                    result = __news_service.search_unreview_list(page)
                                    for index in range(len(result)):
                                        news = result[index]
                                        print(Fore.LIGHTBLUE_EX,
                                              "\n\t%d\t%s\t%s\t%s" % (index + 1, news[1], news[2], news[3]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTRED_EX, "\n\tprev. Prev page")
                                    print(Fore.LIGHTRED_EX, "\n\tnext. Next page")
                                    print(Fore.LIGHTRED_EX, "\n\tback. Back")
                                    print(Style.RESET_ALL)
                                    try:
                                        opt = input("\n\tInput the number: ")
                                        if opt == "prev" and page > 1:
                                            page -= 1
                                        elif opt == "next" and page < count_page:
                                            page += 1
                                        elif opt == "back":
                                            break
                                        elif 1 <= int(opt) <= 5:
                                            news_id = result[int(opt) - 1][0]
                                            __news_service.review_news(news_id)
                                            result = __news_service.search_cache(news_id)
                                            title = result[0]
                                            username = result[1]
                                            type = result[2]
                                            content_id = result[3]
                                            content = __news_service.search_content_by_id(content_id)
                                            if_top = result[4]
                                            create_time = str(result[5])
                                            __news_service.insert(news_id, title, username, type,
                                                                  content, if_top, create_time)
                                    except Exception as e:
                                        print("\n\tInput invalid (Wait 2s)")
                                        time.sleep(2)
                                        continue
                            elif opt == "2":
                                page = 1
                                while True:
                                    os.system("clear")
                                    count_page = __news_service.search_count_page()
                                    result = __news_service.search_list(page)
                                    for index in range(len(result)):
                                        news = result[index]
                                        print(Fore.LIGHTBLUE_EX,
                                              "\n\t%d\t%s\t%s\t%s" % (index + 1, news[1], news[2], news[3]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTRED_EX, "\n\tprev. Prev page")
                                    print(Fore.LIGHTRED_EX, "\n\tnext. Next page")
                                    print(Fore.LIGHTRED_EX, "\n\tback. Back")
                                    print(Style.RESET_ALL)
                                    try:
                                        opt = input("\n\tInput the number: ")
                                        if opt == "prev" and page > 1:
                                            page -= 1
                                        elif opt == "next" and page < count_page:
                                            page += 1
                                        elif opt == "back":
                                            break
                                        elif 1 <= int(opt) <= 5:
                                            news_id = result[int(opt) - 1][0]
                                            __news_service.delete_news(news_id)
                                            __news_service.delete(news_id)
                                    except Exception as e:
                                        print("\n\tInput invalid (Wait 2s)")
                                        time.sleep(2)
                                        continue
                            elif opt == "3":
                                break
                    elif opt == "2":
                        while True:
                            os.system("clear")
                            print(Fore.LIGHTGREEN_EX, "\n\t1. Add users")
                            print(Fore.LIGHTGREEN_EX, "\n\t2. Update users")
                            print(Fore.LIGHTGREEN_EX, "\n\t3. Delete users")
                            print(Fore.LIGHTRED_EX, "\n\t4. Back to account")
                            print(Style.RESET_ALL)
                            opt = input("\n\tInput the number: ")
                            if opt == "1":
                                os.system("clear")
                                username = input("\n\tUsername: ")
                                password = getpass("\n\tPassword: ")
                                repassword = getpass("\n\tRetype password: ")
                                if password != repassword:
                                    print("\n\tPassword not match (Wait 1s)")
                                    time.sleep(1)
                                    continue
                                email = input("\n\tEmail: ")
                                result = __role_service.search_list()
                                for index in range(len(result)):
                                    role = result[index]
                                    print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, role[1]))
                                print(Style.RESET_ALL)
                                opt = input("\n\tInput the role number: ")
                                role_id = result[int(opt) - 1][0]
                                __user_service.add_user(username, password, email, role_id)
                                print("\n\tAdd successfully (Wait 1s)")
                                time.sleep(1)
                            elif opt == "2":
                                page = 1
                                while True:
                                    os.system("clear")
                                    count_page = __user_service.search_count_page()
                                    result = __user_service.search_list(page)
                                    for index in range(len(result)):
                                        user = result[index]
                                        print(Fore.LIGHTBLUE_EX,
                                              "\n\t%d\t%s\t%s" % (index + 1, user[1], user[2]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTRED_EX, "\n\tprev. Prev page")
                                    print(Fore.LIGHTRED_EX, "\n\tnext. Next page")
                                    print(Fore.LIGHTRED_EX, "\n\tback. Back")
                                    print(Style.RESET_ALL)
                                    try:
                                        opt = input("\n\tInput the number: ")
                                        if opt == "prev" and page > 1:
                                            page -= 1
                                        elif opt == "next" and page < count_page:
                                            page += 1
                                        elif opt == "back":
                                            break
                                        elif 1 <= int(opt) <= 5:
                                            os.system("clear")
                                            user_id = result[int(opt) - 1][0]
                                            username = input("\n\tNew username: ")
                                            password = getpass("\n\tNew password: ")
                                            repassword = getpass("\n\tRetype password: ")
                                            if password != repassword:
                                                print("\n\tPassword not match (Wait 1s)")
                                                time.sleep(1)
                                                continue
                                            email = input("\n\tEmail: ")
                                            result = __role_service.search_list()
                                            for index in range(len(result)):
                                                role = result[index]
                                                print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, role[1]))
                                            print(Style.RESET_ALL)
                                            opt = input("\n\tInput the role number: ")
                                            role_id = result[int(opt) - 1][0]
                                            opt = input("\n\tConfirm save(y/n)")
                                            if opt == "Y" or opt == "y":
                                                __user_service.update_user(user_id, username, password, email, role_id)
                                                print("\n\tUpdate successfully (Wait 1s)")
                                                time.sleep(1)
                                    except Exception as e:
                                        print("\n\tInput invalid (Wait 2s)")
                                        time.sleep(2)
                                        continue
                            elif opt == "3":
                                page = 1
                                while True:
                                    os.system("clear")
                                    count_page = __user_service.search_count_page()
                                    result = __user_service.search_list(page)
                                    for index in range(len(result)):
                                        user = result[index]
                                        print(Fore.LIGHTBLUE_EX,
                                              "\n\t%d\t%s\t%s" % (index + 1, user[1], user[2]))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                                    print(Fore.LIGHTBLUE_EX, "\n\t-------------------------")
                                    print(Fore.LIGHTRED_EX, "\n\tprev. Prev page")
                                    print(Fore.LIGHTRED_EX, "\n\tnext. Next page")
                                    print(Fore.LIGHTRED_EX, "\n\tback. Back")
                                    print(Style.RESET_ALL)
                                    try:
                                        opt = input("\n\tInput the number: ")
                                        if opt == "prev" and page > 1:
                                            page -= 1
                                        elif opt == "next" and page < count_page:
                                            page += 1
                                        elif opt == "back":
                                            break
                                        elif 1 <= int(opt) <= 5:
                                            os.system("clear")
                                            user_id = result[int(opt) - 1][0]
                                            __user_service.delete_user(user_id)
                                            print("\n\tDelete successfully (Wait 1s)")
                                            time.sleep(1)
                                    except Exception as e:
                                        print("\n\tInput invalid (Wait 2s)")
                                        time.sleep(2)
                                        continue
                            elif opt == "4":
                                break
                    elif opt == "3":
                        break
                    elif opt == "4":
                        sys.exit(0)
        else:
            print("\n\tLogin failed (Wait 1s)")
            time.sleep(1)
    elif opt == "2":
        sys.exit(0)
