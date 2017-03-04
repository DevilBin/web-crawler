#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Get context from website and send a email.
"""
import core
import mail

if __name__ == "__main__":
    it = core.spider()
    for index in range(1, 8):
        it.getContents(index)
    result = it.retContents()
    try:
        mail.send_email(
            "send email server",
            "send email address",
            "password",
            "to email address",
            "糗事百科笑话抓取",
            result
        )
    except Exception as e:
        print("[E]: Send email error, {0}.".format(e))
    else:
        print("[I]: Send a email succeed.")
