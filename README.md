## ERPNext South Africa

App to hold regional code for South Africa, built on top of ERPNext.

### Introduction

ERPNext South Africa aims to support regional customizations for South Africa. It currently has facility to add South Africa VAT settings, few custom fields, and a report called VAT Audit Report. The app is built on Frappe, a full-stack, meta-data driven, web framework, and integrates seamlessly with ERPNext, the most agile ERP software.

### Installation

Using bench, [install ERPNext](https://github.com/frappe/bench#installation) as mentioned here.

Once ERPNext is installed, add erpnext_south_africa app to your bench by running

```sh
$ bench get-app https://github.com/frappe/erpnext_south_africa.git
```

After that, you can install the app on required site (let's say demo.com )by running

```sh
$ bench --site demo.com install-app erpnext_south_africa
```

### License

GNU GPL V3. See [license.txt](https://github.com/frappe/erpnext_south_africa/blob/develop/license.txt) for more information.

