# ad-security-reports
Test Reports for ADMC and RSAT Elevated Privileges

## Задача
Проверить наличие или отсутствие различий в атрибуте учётной записи **ntSecurityDescriptor**
при выставлении анологичных расширенных прав через оснастку **RSAT** и **ADMC**

## Конфигурация доменной инфраструктуры
1) Домен **EXTRA.ALT** на **samba-4.20.8-alt2.x86_64**
2) #118 **ALT Server P11,  DC1** - контроллер домена **EXTRA.ALT**
3) #143 **Windows 10 22H2, PC1** - клиент для управления доменос с оснасткой **RSAT**
4) #142 **ALT Workstation P11, PC2** - клиент для управления доменос с оснасткой **ADMC**

_**Номера машин в пуле grolda в PROXMOX: #118,#143,#142.**_
