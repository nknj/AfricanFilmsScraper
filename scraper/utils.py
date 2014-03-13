def clean_name_and_desc(name_and_desc):
	cleaned_name_and_desc = []
	for x in name_and_desc:
		x = x.strip()
		if x not in ('About this film:', ''):
			if x.lower().find('click here for') != -1:
				return cleaned_name_and_desc
			cleaned_name_and_desc.append(x)
	return cleaned_name_and_desc

def get_text(tree, xpath_exp):
	return tree.xpath(xpath_exp)[0].text_content().encode('utf-8').strip()