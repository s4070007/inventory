from pymgsql import *
uri='mysql://kulbadz:kul0007@proton.it.kmitl.ac.th/kulbadz?charset=utf8'
connection=connectionForURI(uri)
sqlhub.processConnection=connection

	
#User Table

class Department(Schema):
	class sqlmeta:
		table='department'
	deptname=UnicodeCol(length=50, dbName='deptname' ,notNone=True)	
	User=MultipleJoin('User',joinColumn='department_id')


class User(Schema):
	class sqlmeta:
		table='user'
	username=UnicodeCol(dbName='username',notNone=True, default='')
	title=UnicodeCol(length=20, dbName='title' ,notNone=True, default='')
	first_name=UnicodeCol(length=50, dbName='first_name' ,notNone=True, default='')
	last_name=UnicodeCol(length=50, dbName='last_name' ,notNone=True, default='')	
	supervisor=ForeignKey('User', dbName='supervisor_id',notNone=False,default=None)
	supervisees=MultipleJoin('User',joinColumn='supervisor_id')
	department=ForeignKey('Department' ,dbName='department_id',notNone=False,default=None)
	supervisors=MultipleJoin('Request_doc',joinColumn='supervisor_id')
	dean_requestDocs=MultipleJoin('Request_doc',joinColumn='dean_id')
	request_users=MultipleJoin('Request_doc',joinColumn='request_user_id')
	commercial_numbers=MultipleJoin('Committee_list',joinColumn='user_id')
	loan_agreements=MultipleJoin('Loan_agreement',joinColumn='head_finance_id')
	inventory_user_ids=MultipleJoin('Request_report',joinColumn='inventory_user_id')
	dean_ids=MultipleJoin('Request_report',joinColumn='dean_id')
	requestUser_ids=MultipleJoin('Request_report',joinColumn='request_user_id')
	goodsReceiveds=MultipleJoin('Goods_received',joinColumn='receive_user')
	borrowers=MultipleJoin('Borrow_assets',joinColumn='user_id')
	borrows=MultipleJoin('Borrow_assets',joinColumn='inventory_user_id')
	borrow_assets_details=MultipleJoin('Borrow_assets_detail',joinColumn='return_user')
	approving_user_as=MultipleJoin('Assets_dispense',joinColumn='approving_user')
	disposing_user_as=MultipleJoin('Assets_dispense',joinColumn='disposing_user')
	approving_user_ms=MultipleJoin('Material_dispense',joinColumn='approving_user')
	disposing_user_ms=MultipleJoin('Material_dispense',joinColumn='disposing_user')
	user_out_materials=MultipleJoin('Out_material',joinColumn='user_id')
	fining_users=MultipleJoin('Contract_fine',joinColumn='fining_user')	

	
	
class Inventory_group(Schema):
	class sqlmeta:
		table='inventory_group'
	group_name=UnicodeCol(length=200, dbName='group_name' ,notNone=True)
	inventory_type=UnicodeCol(length=50, dbName='inventory_type' ,notNone=True)
	vendor=MultipleJoin('Vendor' ,joinColumn='inventory_group_id')
	request_doc=MultipleJoin('Request_doc' ,joinColumn='inventory_group_id')
	request_order=MultipleJoin('Purchase_order' ,joinColumn='inventory_group_id')
	goods_received=MultipleJoin('Goods_received' ,joinColumn='inventory_group_id')
	assets=MultipleJoin('Assets' ,joinColumn='inventory_group_id')
	material=MultipleJoin('Material' ,joinColumn='inventory_group_id')	
	
class Vendor(Schema):
	class sqlmeta:
		table='vendor'
	vendor_name=UnicodeCol(length=200, dbName='vendor_name' ,notNone=True, default='')
	commercial_number=UnicodeCol(length=50, dbName='commercial_number' ,notNone=True, default='')
	type_business=ForeignKey('Inventory_group' ,dbName='inventory_group_id',notNone=False,default=None)
	agent_first_name=UnicodeCol(length=50, dbName='agent_first_name', default='')
	agent_last_name=UnicodeCol(length=50, dbName='agent_last_name', default='')
	contact_number=UnicodeCol(length=10, dbName='contact_number', default='')
	address_number=UnicodeCol(length=50, dbName='address_number', default='')
	road=UnicodeCol(length=50, dbName='road', default='')
	tambon=UnicodeCol(length=50, dbName='tambon', default='')
	distinc=UnicodeCol(length=50, dbName='distinc', default='')	
	provinc=UnicodeCol(length=50, dbName='provinc', default='')
	post_code=UnicodeCol(length=5, dbName='postCode', default='')
	phone_number=UnicodeCol(length=10, dbName='phone_number', default='')
	fax=UnicodeCol(length=10, dbName='fax', default='')
	email=UnicodeCol(dbName='email', default='')
	website=UnicodeCol(dbName='website', default='')
	quotation=MultipleJoin('Quotation', joinColumn='vendor_id')
	purchase_order=MultipleJoin('Purchase_order', joinColumn='vendor_id')
	request_report=MultipleJoin('Request_report', joinColumn='vendor_id')
	
class Request_doc(Schema):
	class sqlmeta:
		table='request_doc'
	request_doc_no=UnicodeCol(length=50, dbName='request_doc_no' ,notNone=True)
	doc_date=DateTimeCol(default=None, dbName='doc_date')
	name_request=UnicodeCol(dbName='name_request' ,notNone=True)
	inventory_group_id=ForeignKey('Inventory_group' ,dbName='inventory_group_id',notNone=False,default=None)
	reason=UnicodeCol(dbName='reason' ,notNone=True)
	type_pay=UnicodeCol(length=50, dbName='type_pay' ,notNone=True)
	total_price=FloatCol(dbName='total_price' ,default=0 ,notNone=True)
	tax=FloatCol(dbName='tax', default=7 ,notNone=True)
	budget_year=IntCol(dbName='budget_year',default=0,notNone=True)
	approved_date=DateTimeCol(dbName=None, notNone=True,default=None)
	status=UnicodeCol(dbName='status' ,default='')
	supervisor=ForeignKey('User' ,dbName='supervisor_id' ,notNone=False,default=None)
	dean=ForeignKey('User' ,dbName='dean_id' ,notNone=False,default=None)
	request_user=ForeignKey('User' ,dbName='request_user_id' ,notNone=False,default=None)
	request_doc_detail=MultipleJoin('Request_doc_detail' ,joinColumn='request_doc_id')
	financial_code=MultipleJoin('Financial_code' ,joinColumn='request_doc_id')
	committee_list=MultipleJoin('Committee_list' ,joinColumn='request_doc_id')
	quotation=MultipleJoin('Quotation' ,joinColumn='request_doc_id')
	specification=MultipleJoin('Specification' ,joinColumn='request_doc_id')
	loan_agreement=MultipleJoin('Loan_agreement' ,joinColumn='request_doc_id')
	

class Request_doc_detail(Schema):
	class sqlmeta:
		table='request_doc_detail'
	inventory_name=UnicodeCol(length=200, dbName='inventory_name' ,notNone=True ,default='')
	price=FloatCol(dbName='price' ,default=0)
	unit=IntCol(dbName='unit' ,default=0)
	count_unit=UnicodeCol(length=50, dbName='count_unit' ,notNone=True ,default='')
	amount=FloatCol(dbName='amount' ,default=0)
	request_doc_id=ForeignKey('Request_doc', dbName='request_doc_id' ,notNone=True)
	
class Financial_code(Schema):
	class sqlmeta:
		table='financial_code'
	faculty=UnicodeCol(length=2, dbName='faculty' ,notNone=True ,default='')
	major=UnicodeCol(length=5, dbName='major' ,default='')
	academic_service=UnicodeCol(length=5, dbName='academic_service' ,default='')
	fund=UnicodeCol(length=4, dbName='fund' ,default='')
	plan=UnicodeCol(length=5, dbName='plan' ,default='') 
	main_activity=UnicodeCol(length=4, dbName='main_activity' ,default='')
	second_activity=UnicodeCol(length=2, dbName='second_activity' ,default='')
	sub_activity=UnicodeCol(length=3, dbName='sub_activity' ,default='')
	payment=UnicodeCol(length=5, dbName='payment' ,default='')
	payment_type=UnicodeCol(length=5, dbName='payment_type' ,default='')
	request_doc_id=ForeignKey('Request_doc', dbName='request_doc_id' ,notNone=False,default=None)
	payment_f=UnicodeCol(length=100, dbName='payment_f' ,default='')
	payment_code_f=UnicodeCol(length=100, dbName='payment_code_f' ,default='')
	
class Committee_list(Schema):
	class sqlmeta:
		table='committee_list'	
	request_doc=ForeignKey("Request_doc", dbName="request_doc_id" ,notNone=False,default=None)
	user=ForeignKey("User", dbName="user_id",notNone=False,default=None)
	fk=DatabaseIndex("request_doc", "user", unique=True)
		
		
class Quotation(Schema):
	class sqlmeta:
		table='quotation'
	doc_date=DateTimeCol(dbName='doc_date', default=None)
	quotation=BLOBCol(dbName='quotation', default=None, length=2**16, varchar=False)
	file_name=UnicodeCol(length=200, dbName='file_name',default='')
	request_doc_id=ForeignKey('Request_doc', dbName='request_doc_id' ,notNone=False,default=None)
	vendor=ForeignKey('Vendor', dbName='vendor_id',notNone=False,default=None)
	purchase_order=MultipleJoin('Purchase_order', joinColumn='quotation_id')
	
	
class Specification(Schema):
	class sqlmeta:
		table='specification'
	doc_date=DateTimeCol(default=None, dbName='doc_date')
	specification=BLOBCol(dbName='specification', default=None, length=2**16, varchar=False)
	file_name=UnicodeCol(length=200, dbName='file_name' ,notNone=True, default='')
	request_doc_id=ForeignKey('Request_doc', dbName='request_doc_id' ,notNone=False,default=None)
	
	
class Loan_agreement(Schema):
	class sqlmeta:
		table='loan_agreement'
	loan_no=UnicodeCol(length=50 ,dbName='loan_no' ,notNone=True, default='')
	amount=FloatCol(dbName='amount', default=0, notNone=True)
	due_date=DateTimeCol(default=None, dbName='due_date')
	borrow_book=BLOBCol(dbName='borrow_book', default=None, length=2**16, varchar=False)
	file_name=UnicodeCol(length=200, dbName='file_name', notNone=True, default='')
	doc_date=DateTimeCol(default=None, dbName='doc_date')
	finance_date=DateTimeCol(default=None, dbName='finance_date')
	dean_date=DateTimeCol(default=None, dbName='dean_date')
	receive_date=DateTimeCol(default=None, dbName='receive_date')
	request_doc_id=ForeignKey('Request_doc',dbName='request_doc_id' ,notNone=False,default=None)
	head_finance=ForeignKey('User', dbName='head_finance_id',notNone=False,default=None)
	
class Request_report(Schema):
	class sqlmeta:
		table='requestReport'
	request_report_no=UnicodeCol(length=50, dbName='request_report_no' ,notNone=True, default='')
	division=UnicodeCol(length=100, dbName='division', default='')
	doc_date=DateTimeCol(dbName='doc_date', default=None)
	name_request=UnicodeCol(length=200, dbName='name_request' ,notNone=True, default='')
	inventory_group_id=ForeignKey('Inventory_group' ,dbName='inventory_group_id' ,notNone=False,default=None)
	reason=UnicodeCol(length=500, dbName='reason' ,notNone=True, default='')
	type_pay=UnicodeCol(length=50, dbName='type_pay' ,notNone=True, default='')
	total_price=FloatCol(dbName='total_price', default=0)
	tax=FloatCol(dbName='tax', default=0)
	budget_year=IntCol(dbName='budget_year', default=0)
	approved_date=DateTimeCol(dbName='approved_date', default=None)
	status=UnicodeCol(length=200, dbName='status' ,notNone=True, default='')	
	inventory_user_id=ForeignKey('User', dbName='inventory_user_id',notNone=False,default=None)
	dean_id=ForeignKey('User', dbName='dean_id',notNone=False,default=None)
	request_user_id=ForeignKey('User', dbName='request_user_id',notNone=False,default=None)
	request_report_detail=MultipleJoin('Request_report_detail', joinColumn='request_report_id')
	purchase_order=MultipleJoin('Purchase_order', joinColumn='request_report_id')
	vendor_id=ForeignKey('Vendor', dbName='vendor_id',notNone=False,default=None)
	
	
	
	
class Request_report_detail(Schema):
	class sqlmeta:
		table='request_report_detail'
	inventory_name=UnicodeCol(length=200, dbName='inventory_name' ,notNone=True, default='')
	price=FloatCol(dbName='price', default=0)
	previous_price=FloatCol(dbName='previous_price', default=0)
	unit=IntCol(dbName='unit', default=0)
	count_unit=UnicodeCol(length=50, dbName='count_unit' ,notNone=True, default='')
	amount=FloatCol(dbName='amount')
	request_report_id=ForeignKey('Request_report',notNone=True, dbName='request_report_id')
	
class Purchase_order(Schema):
	class sqlmeta:
		table='purchase_order'
	purchase_order_no=UnicodeCol(length=200, dbName='purchase_orderNo' ,notNone=True, default='')
	book_no=UnicodeCol(length=50, dbName='book_no' ,notNone=True, default='')
	doc_date=DateTimeCol(dbName='doc_date', default=None)
	due_date=DateTimeCol(dbName='due_date', default=None)
	payment_condition=UnicodeCol(length=50, dbName='payment_condition' ,notNone=True, default='')
	due_time=UnicodeCol(length=50, dbName='due_time' ,notNone=True, default='')
	deliveried_place=UnicodeCol(length=200 ,dbName='deliveried_place' ,notNone=True, default='')
	tax=FloatCol(dbName='tax', default=0)
	total_price=FloatCol(dbName='total_price', default=0)
	text_price=UnicodeCol(length=200 ,dbName='text_price' ,notNone=True, default='')
	vendor_id=ForeignKey('Vendor', dbName='vendor_id',notNone=False,default=None)
	request_report_id=ForeignKey('Request_report' ,dbName='request_report_id',notNone=False,default=None)
	quotation_id=ForeignKey('Quotation' ,dbName='quotation_id',notNone=False,default=None)
	inventory_group_id=ForeignKey('Inventory_group' ,dbName='inventory_group_id',notNone=False,default=None)
	purchase_order_detail=MultipleJoin('Purchase_order_detail' ,joinColumn='purchase_order_id')
	goods_received=MultipleJoin('goods_received' ,joinColumn='purchase_order_id')
	contract=MultipleJoin('Contract' ,joinColumn='purchase_order_id')

class Purchase_order_detail(Schema):
	class sqlmeta:
		table='purchase_order_detail'
	inventory_name=UnicodeCol(length=200, dbName='inventory_name' ,notNone=True)
	price=FloatCol(dbName='price', default=0)
	unit=IntCol(dbName='unit', default=0)
	count_unit=UnicodeCol(length=50, dbName='count_unit' ,notNone=True, default='')
	amount=FloatCol(dbName='amount', default=0)
	status_register=UnicodeCol(length=200, dbName='status_register' ,notNone=True, default='')
	purchase_order_id=ForeignKey('Purchase_order', notNone=True, dbName='purchase_order_id')
	
class Goods_received(Schema):
	class sqlmeta:
		table='goods_received'
	invoice_no=UnicodeCol(length=200, dbName='invoice_no' ,notNone=True, default='')
	receive_date=DateTimeCol(dbName='receive_date', default=None)
	tax=FloatCol(dbName='tax', default=0)
	total_price=FloatCol(dbName='total_price', default=0)
	invoice=BLOBCol(dbName='invoice', length=2**16, varchar=False, default=None)
	file_name=UnicodeCol(length=200, dbName='file_name' ,notNone=True, default='')
	purchase_order_id=ForeignKey('Purchase_order', dbName='purchase_order_id',notNone=False,default=None)
	inventory_group_id=ForeignKey('Inventory_group', dbName='inventory_group_id',notNone=False,default=None)
	receive_user=ForeignKey('User', dbName='receive_user',notNone=False,default=None)
	goods_received_assets=MultipleJoin('Goods_received_assets', joinColumn='goods_received_id')
	goods_received_material=MultipleJoin('Goods_received_material', joinColumn='goods_received_id')
	upload_file=MultipleJoin('Upload_file', joinColumn='goods_received_id')
	
	
class Assets(Schema):
	class sqlmeta:
		table='assets'
	brand=UnicodeCol(length=200 ,dbName='brand' ,notNone=True, default='')
	version=UnicodeCol(length=200 ,dbName='version' ,notNone=True, default='')
	assets_title=UnicodeCol(length=200, dbName='assets_title' ,notNone=True, default='')
	assets_detail=UnicodeCol(length=200, dbName='assets_detail' ,notNone=True, default='')
	total_unit=IntCol(dbName='total_unit', default=0)
	count_unit=UnicodeCol(length=50, dbName='count_unit' ,notNone=True, default='')
	price_per_unit=FloatCol(dbName='price_per_unit', default=0)
	image=BLOBCol(dbName='image', length=2**16, varchar=False, default=None)
	file_name=UnicodeCol(length=200, dbName='file_name' ,notNone=True, default='')
	inventory_group_id=ForeignKey('Inventory_group',dbName='inventory_group_id',notNone=False,default=None)
	goods_received_assets=MultipleJoin('Goods_received_assets', joinColumn='assets_id')
	register_code=MultipleJoin('Register_code', joinColumn='assets_id')
	idAssets=MultipleJoin('Id_assets', joinColumn='assets_id')
	
	
class Goods_received_assets(Schema):
	class sqlmeta:
		table='goods_received_assets'
	detail=UnicodeCol(length=200 ,dbName='detail' ,notNone=True ,default='')
	amount=FloatCol(dbName='amount' ,default=0)
	price=FloatCol(dbName='price' ,default=0)
	tax=FloatCol(dbName='tax' ,default=7)
	unit=IntCol(dbName='unit' ,default=0)
	count_unit=UnicodeCol(length=50, dbName='count_unit' ,notNone=True ,default='')
	status_register=UnicodeCol(length=200, dbName='status_register' ,notNone=True ,default='')
	goods_received_id=ForeignKey('Goods_received' ,dbName='goods_received_id',notNone=False,default=None)
	assets_id=ForeignKey('Assets' ,dbName='assets_id',notNone=False,default=None)
	
class Register_code(Schema):
	class sqlmeta:
		table='register_code'
	faculty=UnicodeCol(length=2 ,dbName='faculty' ,notNone=True, default='')
	major=UnicodeCol(length=5, dbName='major', default='')
	academic_service=UnicodeCol(length=5, dbName='academic_service', default='')
	fund=UnicodeCol(length=4, dbName='fund', default='')
	plan=UnicodeCol(length=5, dbName='plan', default='') 
	main_activity=UnicodeCol(length=4, dbName='main_activity', default='')
	second_activity=UnicodeCol(length=2, dbName='second_activity', default='')
	sub_activity=UnicodeCol(length=3, dbName='sub_activity', default='')
	payment=UnicodeCol(length=5, dbName='payment', default='')
	payment_type=UnicodeCol(length=5, dbName='payment_type', default='')
	assets_id=ForeignKey('Assets' ,dbName='assets_id',notNone=False,default=None)
	
	
class Id_assets(Schema):
	class sqlmeta:
		table='id_assets'
	assets_no=UnicodeCol(length=200, dbName='assets_no', notNone=True, unique=True, default='')
	assets_status=UnicodeCol(length=50, dbName='assets_status' ,notNone=True, default='')
	assets_id=ForeignKey('Assets', notNone=True ,dbName='assets_id')
	borrow_assets_detail=MultipleJoin('Borrow_assets_detail', joinColumn='id_assets_id')
	assets_dispense_detail=MultipleJoin('Assets_dispense_detail', joinColumn='id_assets_id')
	repairing=MultipleJoin('Repairing' ,joinColumn='id_assets_id')
	super_set=ForeignKey('Id_assets', dbName='super_set_id',notNone=False,default=None)
	subset=MultipleJoin('Id_assets',joinColumn='super_set_id')
	
	
class Borrow_assets(Schema):
	class sqlmeta:
		table='borrow_assets'
	borrow_date=DateTimeCol(dbName='borrow_date' ,default=None)
	doc_date=DateTimeCol(dbName='doc_date', default=None)
	user_id=ForeignKey('User', dbName='user_id',notNone=False,default=None)
	inventory_user_id=ForeignKey('User', dbName='inventory_user_id',notNone=False,default=None)
	borrow_assets_detail=MultipleJoin('Borrow_assets_detail', joinColumn='borrow_assets_id')
	
class Borrow_assets_detail(Schema):
	class sqlmeta:
		table='borrow_assets_detail'
	due_date=DateTimeCol(dbName='due_date' ,default=None)
	return_date=DateTimeCol(dbName='return_date' ,default=None)
	doc_date=DateTimeCol(dbName='doc_date' ,default=None)
	area=UnicodeCol(length=200, dbName='area', notNone=True, default='')
	note=UnicodeCol(dbName='note', default='')
	return_user=ForeignKey('User', dbName='return_user',notNone=False,default=None)
	borrow_assets_id=ForeignKey('Borrow_assets' ,dbName='borrow_assets_id',notNone=False,default=None)
	id_assets_id=ForeignKey('Id_assets', dbName='id_assets_id',notNone=False,default=None)
	
class Assets_dispense(Schema):
	class sqlmeta:
		table='assets_dispense'
	assets_dispense_no=UnicodeCol(length=200, dbName='assets_dispense_no' ,notNone=True)
	doc_date=DateTimeCol(dbName='doc_date')
	taken_date=DateTimeCol(dbName='taken_date')
	dispense_reason=UnicodeCol(length=200, dbName='dispense_reason' ,notNone=True)
	method=UnicodeCol(length=200, dbName='method')
	receiver=UnicodeCol(length=200, dbName='receiver')
	evidence=BLOBCol(dbName='evidence' ,length=2**16, varchar=False)
	file_name=UnicodeCol(length=200, dbName='file_name' ,notNone=True)
	approving_user=ForeignKey('User' ,dbName='approving_user',notNone=False,default=None)
	disposing_user=ForeignKey('User' ,dbName='disposing_user',notNone=False,default=None)
	assets_dispense_detail=MultipleJoin('Assets_dispense_detail', joinColumn='assets_dispense_id')
	
	
	
class Assets_dispense_detail(Schema):
	class sqlmeta:
		table='assets_dispense_detail'
		assets_dispense_id=ForeignKey('Assets_dispense' ,dbName='assets_dispense_id',notNone=False,default=None)
		id_assets_id=ForeignKey('Id_assets', dbName='id_assets_id',notNone=False,default=None)
		fk=DatabaseIndex("assets_dispense", "id_assets", unique=True)
		

class Material(Schema):
	class sqlmeta:
		table='material'
	material_name=UnicodeCol(length=200, dbName='material_name' ,notNone=True ,default='')
	detail=UnicodeCol(length=200, dbName='detail' ,default='')
	on_hand=IntCol(dbName='on_hand' ,default=0)
	minimum_stock=IntCol(dbName='minimum_stock' ,default=0)
	count_unit=UnicodeCol(length=50, dbName='count_unit' ,notNone=True ,default='')
	price_per_unit=FloatCol(dbName='price_per_unit' ,default=0)
	image=BLOBCol(dbName='image', length=2**16, varchar=False ,default=None)
	file_name=UnicodeCol(length=200, dbName='file_name' ,notNone=True ,default='')
	inventory_group_id=ForeignKey('Inventory_group' ,dbName='inventory_group_id',notNone=False,default=None)
	goods_received_material=MultipleJoin('Goods_received_material', joinColumn='material_id')
	material_dispense_detail=MultipleJoin('Material_dispense_detail', joinColumn='material_id')
	out_material_detail=MultipleJoin('Out_material_detail', joinColumn='material_id')
	
	
class Goods_received_material(Schema):
	class sqlmeta:
		table='goods_received_material'
	detail=UnicodeCol(length=200 ,dbName='detail' ,notNone=True ,default='')
	amount=FloatCol(dbName='amount' ,default=0)
	price=FloatCol(dbName='price' ,default=0)
	tax=FloatCol(dbName='tax' ,default=7)
	unit=IntCol(dbName='unit' ,default=0)
	count_unit=UnicodeCol(length=50, dbName='count_unit' ,notNone=True ,default='')
	status_register=UnicodeCol(length=200, dbName='status_register' ,notNone=True ,default='')
	goods_received_id=ForeignKey('Goods_received', notNone=True ,dbName='goods_received_id')
	material_id=ForeignKey('Material' ,dbName='material_id',notNone=False,default=None)
	
class Material_dispense(Schema):
	class sqlmeta:
		table='material_dispense'
	material_dispenseNo=UnicodeCol(length=200, dbName='assets_dispense' ,notNone=True, default='')
	doc_date=DateTimeCol(dbName='doc_date', default=None)
	taken_date=DateTimeCol(dbName='taken_date', default=None)
	dispense_reason=UnicodeCol(length=200, dbName='dispense_reason' ,notNone=True, default='')
	method=UnicodeCol(length=200, dbName='method', default='')
	receiver=UnicodeCol(length=200, dbName='receiver', default='')
	evidence=BLOBCol(dbName='evidence', length=2**16, varchar=False, default=None)
	file_ame=UnicodeCol(length=200, dbName='file_name' ,notNone=True, default='')
	approving_user=ForeignKey('User' ,dbName='approving_user',notNone=False,default=None)
	disposing_user=ForeignKey('User', dbName='disposing_user',notNone=False,default=None)
	material_dispense_detail=MultipleJoin('Material_dispense_detail' ,joinColumn='material_dispense_id')
	
	
class Material_dispense_detail(Schema):
	class sqlmeta:
		table='materialDispenseDetail'
	unit=IntCol(dbName='unit', notNone=True, default=0)
	material_dispense_id=ForeignKey('Material_dispense', notNone=True ,dbName='material_dispense_id')
	material_id=ForeignKey('Material', dbName='material_id',notNone=False,default=None)
	
	
class Out_material(Schema):
	class sqlmeta:
		table='out_material'
	date_out_material=DateTimeCol(dbName='date_out_material', default=None)
	user_id=ForeignKey('User', dbName='user_id',notNone=False,default=None)
	out_material_detail=MultipleJoin('Out_material_detail', joinColumn='out_material_id')

	
	
class Out_material_detail(Schema):
	class sqlmeta:
		table='out_material_detail'
	unit=IntCol(dbName='unit' ,default=None)
	note=UnicodeCol(dbName='note',default='')
	material_id=ForeignKey('Material' ,dbName='material_id',notNone=False,default=None)
	out_material_id=ForeignKey('Out_material' ,dbName='out_material_id',notNone=False,default=None)
	
	
class Contract(Schema):
	class sqlmeta:
		table='contract'
	contract_no=UnicodeCol(length=200, dbName='contractNo' ,notNone=True ,unique=True)
	due_date=DateTimeCol(dbName='due_date', default=None)
	doc_date=DateTimeCol(dbName='doc_date', default=None)
	detail=UnicodeCol(length=200, dbName='detail' ,default='')
	purchase_order_id=ForeignKey('Purchase_order' ,dbName='purchase_order_id',notNone=False,default=None)
	contract_fine=MultipleJoin('contractFine' ,joinColumn='contract_id')
	
class Contract_fine(Schema):
	class sqlmeta:
		table='contract_fine'
	doc_date=DateTimeCol(dbName='doc_date' ,default=None)
	num_date_late=IntCol(dbName='num_date' ,default=0)
	fine=FloatCol(dbName='fine' ,default=0)
	pay_fine_status=UnicodeCol(length=50, dbName='pay_fine_status', notNone=True ,default='')
	reason=UnicodeCol(dbName='reason' ,default='')
	contract_id=ForeignKey('Contract' ,dbName='contract_id',notNone=False,default=None)
	fining_user_id=ForeignKey('User' ,dbName='fining_user',notNone=False,default=None)
	
class Upload_file(Schema):
	class sqlmeta:
		table='upload_file'
	image=BLOBCol(dbName='iamge', length=2**16, varchar=False, default=None)
	file_name=UnicodeCol(length=200, dbName='file_name' ,notNone=True, default='')
	goods_received_id=ForeignKey('Goods_received', notNone=True, dbName='goods_received_id')
	
class Repairing(Schema):
	class sqlmeta:
		table='repairing'
	detail=UnicodeCol(dbName='detail' ,notNone=True, default='')
	repair_cost=FloatCol(dbName='repair_cost', default=0)
	repair_date=DateTimeCol(dbName='repair_date', default=None)
	doc_date=DateTimeCol(dbName='doc_date' , default=None)
	end_date=DateTimeCol(dbName='end_date', default=None)
	repair_invoice=BLOBCol(dbName='repair_invoice', length=2**16, varchar=False, default=None)
	file_name=UnicodeCol(length=200, dbName='file_name' ,notNone=True, default='')
	id_assets_id=ForeignKey('Id_assets', dbName='id_assets_id',notNone=False,default=None)


	
	
	
		
	
	
	
DB=(Department,User,Inventory_group,Vendor,Request_doc,Request_doc_detail,Financial_code,Committee_list,
Quotation,Specification,Loan_agreement,Request_report,Request_report_detail,Purchase_order,Purchase_order_detail
,Goods_received,Assets,Goods_received_assets,Register_code,Id_assets,Borrow_assets,Borrow_assets_detail,
Assets_dispense,Assets_dispense_detail,Material,Goods_received_material,Material_dispense,Material_dispense_detail,
Out_material,Out_material_detail,Contract,Contract_fine,Upload_file,Repairing)




for table in DB[::-1]: table.dropTable(ifExists=True)
for table in DB: table.createTable(ifNotExists=True)




