---
title: DKIM set up
slug: "dkim-set-up"
source_url: "https://help.mindbox.ru/docs/dkim-set-up"
vcs_path: "dkim-set-up.md"
toc_path:
  - Рассылки
  - "Email-рассылки"
  - Дополнительные возможности рассылок
  - Цифровые подписи
fetched_at: "2026-05-04T11:22:58Z"
content_hash: "sha256:fb940e3ee080c75901bbbd907627436ac7f5bde4644f1542d1a62cc73232a3cd"
---

# DKIM set up

## Overview

[Русская версия статьи](как-настроить-dkim-и-dmarc)

DKIM (DomainKeys Identified Mail) is an important authentication mechanism to help protect both email receivers and email senders from forged and phishing email.

DKIM records are a TXT record that is part of a domain's DNS zone file. The TXT record specifies a list of authorized host names/IP addresses that mail can originate from for a given domain name.  
How it works:

1. Recipient mail server receives a letter from some email address (for example, [info@company.com](mailto:info@company.com) ) with the sender server - mta.mindbox.ru
2. Recipient's server makes a request to the DNS of company.com trying to find DKIM records

   - It does not exist. Letter status becomes «neutral». It means that some extra spam tests required for this letter.
   - It does exist. Does [mta.mindbox.ru](http://mta.mindbox.ru/) allow to send a letter for [info@company.com](mailto:info@company.com):

     - Yes - letter status becomes «pass». Generally it means that no special spam tests required for this letter.
     - No - letter status becomes «neutral». See 2a for more details.

The following is an example of DNS record:

![x1.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/x1.png)

Important! The second-level domain for DKIM is automatically inserted!  
For example, if the key is added for the [company.com](http://company.com/) domain, then the entry must be of the form mindbox._domainkey, and if for the domain mail.company.com, the entry must be mindbox._domainkey.mail

## DKIM set up

Ask your manager to generate the couple of DKIM keys and send you required info (public key and instructions).After you will need to create two TXT records to your DNS server with the obtained information.

![6650400099a18c15ea73b417c4aa91d02017-02-151114001.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/6650400099a18c15ea73b417c4aa91d02017-02-151114001.png)

**IMPORTANT** : The key must be only one string! Delete all line breaks if key contains them.

#### DKIM check

Validate your settings using [this service](http://www.mail-tester.com/spf-dkim-check).  
If all set up correctlyyou should see something like this:

![665040012f715a5c2d21f190a7076df3Img19-04-201611-00-10.jpg](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/665040012f715a5c2d21f190a7076df3Img19-04-201611-00-10.jpg)

It means that everything right on your side.

The next step is to checkMindbox’s server settings. Send an email from Mindbox platform to GMail and check the headings of the letter:

![665040031fd569e52655ccc56b14f762gmail.png](https://storage.yandexcloud.net/assets-help-mindbox-ru/images/665040031fd569e52655ccc56b14f762gmail.png)

Look for DKIM headers

Status “dkim=pass” means everything is ok.

If “dkim=neutral” or “dkim=fail” – please ask your manager for help.

[Зачем нужна политика DMARC](https://mindbox.ru/academy/education/politika-dmarc/). Правила проверки email-рассылок и как ее внедрить.
