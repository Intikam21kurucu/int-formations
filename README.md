# int-formations
Social Media Users İnfos For intikam21 Cyber/

# Turkish

# Intikam21 Cyber Team - Social Information Tool Sorumluluk Kabulü

## Sorumluluk Reddi
Bu araç, yalnızca yasal siber güvenlik testleri ve eğitim amaçlı kullanılmak üzere tasarlanmıştır. Kullanıcılar, bu aracı yalnızca yetki verilmiş sistemler üzerinde ve yasal izinle kullanmayı kabul ederler. "Intikam21 Cyber Team" ve aracın yaratıcıları, bu aracın kötüye kullanılmasından kaynaklanabilecek herhangi bir zarar, kayıp veya yasal sorunlardan sorumlu tutulamaz.

## Kullanım Koşulları
1. Kullanıcılar, bu aracı kullanarak elde ettikleri bilgileri yasa dışı veya etik olmayan amaçlar için kullanmayacaklarını kabul ederler.
2. Kullanıcılar, bu aracın kullanımı sırasında üçüncü şahısların gizliliğini ihlal etmeyeceklerini taahhüt ederler.
3. Kullanıcılar, bu aracı kullanırken karşılaşabilecekleri herhangi bir teknik sorundan "Intikam21 Cyber Team" veya aracın yaratıcılarını sorumlu tutmayacaklarını kabul ederler.

## Kabul ve Onay
Bu aracı kullanarak, yukarıdaki şartları ve koşulları kabul etmiş olursunuz. Eğer bu şartları kabul etmiyorsanız, lütfen aracı kullanmayınız.

[GitHub'da Sorumluluk Kabulü'nü Onayla]

----------------------------------------

# English

# Intikam21 Cyber Team - Social Information Tool Liability Acceptance

## Disclaimer of Liability
This tool is designed solely for legal cybersecurity testing and educational purposes. Users agree to use this tool only on authorized systems and with legal permission. "Intikam21 Cyber Team" and the creators of this tool cannot be held responsible for any damage, loss, or legal issues arising from misuse of this tool.

## Terms of Use
1. Users agree not to use the information obtained through this tool for illegal or unethical purposes.
2. Users commit not to violate the privacy of third parties during the use of this tool.
3. Users agree not to hold "Intikam21 Cyber Team" or the creators of this tool responsible for any technical issues that may arise during the use of this tool.

## Acceptance and Approval
By using this tool, you accept the above terms and conditions. If you do not accept these terms, please do not use the tool.

[Approve Liability Acceptance on GitHub]

# Kurulum Talimatları / Installation Instructions

Bu belge, Intikam21 Cyber Team'in Social Information aracının Termux ve Kali Linux üzerinde nasıl kurulacağını açıklamaktadır. / This document outlines how to install the Social Information tool by Intikam21 Cyber Team on Termux and Kali Linux.

## Termux için Kurulum / Installation on Termux

Termux, Android cihazlar için bir terminal emülatörü ve Linux ortamıdır. / Termux is a terminal emulator and Linux environment for Android devices. Aşağıdaki adımları izleyerek Social Information aracını Termux üzerinde kurabilirsiniz: / Follow these steps to install the Social Information tool on Termux:

1. Termux uygulamasını açın. / Open the Termux app.
2. Paket listesini güncellemek için `pkg update` komutunu girin. / Update the package list with the command: `pkg update`.
3. Python ve pip yüklemek için `pkg install python` komutunu girin. / Install Python and pip with the command: `pkg install python`.
4. Gerekli kütüphaneleri yüklemek için aşağıdaki pip komutlarını kullanın: / Install the required libraries using the following pip commands:
````pip install googleapiclient
pip install os
pip install time
pip install pyfiglet
pip install requests
```` or :
`chmod +x install.sh`
`./install.sh`
