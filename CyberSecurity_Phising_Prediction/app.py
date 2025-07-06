import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression


st.title( 'Cubersecurity Phising Detection using Machine Learning')

model = pickle.load(open('D:\\data_science_repo\\CyberSecurity_Phising_Prediction\\model.pkl','rb'))

length_url = st.number_input('length_url')
length_hostname = st.number_input('length_hostname')
ip = st.number_input('ip')
nb_dots = st.number_input('nb_dots')
nb_hyphens = st.number_input('nb_hyphens')
nb_at = st.number_input('nb_at')
nb_qm = st.number_input('nb_qm')
nb_and = st.number_input('nb_and')
nb_or = st.number_input('nb_or')
nb_eq = st.number_input('nb_eq')
nb_underscore = st.number_input('nb_underscore')
nb_tilde = st.number_input('nb_tilde')
nb_percent = st.number_input('nb_percent')
nb_slash = st.number_input('nb_slash')
nb_star = st.number_input('nb_star')
nb_colon = st.number_input('nb_colon')
nb_comma = st.number_input('nb_comma')
nb_semicolumn = st.number_input('nb_semicolumn')
nb_dollar = st.number_input('nb_dollar')
nb_space = st.number_input('nb_space')
nb_www = st.number_input('nb_www')
nb_com = st.number_input('nb_com')
nb_dslash = st.number_input('nb_dslash')
http_in_path = st.number_input('http_in_path')
https_token = st.number_input('https_token')
ratio_digits_url = st.number_input('ratio_digits_url')
ratio_digits_host = st.number_input('ratio_digits_host')
punycode = st.number_input('punycode')
port = st.number_input('port')
tld_in_path = st.number_input('tld_in_path')
tld_in_subdomain = st.number_input('tld_in_subdomain')
abnormal_subdomain = st.number_input('abnormal_subdomain')
nb_subdomains = st.number_input('nb_subdomains')
prefix_suffix = st.number_input('prefix_suffix')
random_domain = st.number_input('random_domain')
shortening_service = st.number_input('shortening_service')
path_extension = st.number_input('path_extension')
nb_redirection = st.number_input('nb_redirection')
nb_external_redirection = st.number_input('nb_external_redirection')
length_words_raw = st.number_input('length_words_raw')
char_repeat = st.number_input('char_repeat')
shortest_words_raw = st.number_input('shortest_words_raw')
shortest_word_host = st.number_input('shortest_word_host')
shortest_word_path = st.number_input('shortest_word_path')
longest_words_raw = st.number_input('longest_words_raw')
longest_word_host = st.number_input('longest_word_host')
longest_word_path = st.number_input('longest_word_path')
avg_words_raw = st.number_input('avg_words_raw')
avg_word_host = st.number_input('avg_word_host')
avg_word_path = st.number_input('avg_word_path')
phish_hints = st.number_input('phish_hints')
domain_in_brand = st.number_input('domain_in_brand')
brand_in_subdomain = st.number_input('brand_in_subdomain')
brand_in_path = st.number_input('brand_in_path')
suspecious_tld = st.number_input('suspecious_tld')
statistical_report = st.number_input('statistical_report')
nb_hyperlinks = st.number_input('nb_hyperlinks')
ratio_intHyperlinks = st.number_input('ratio_intHyperlinks')
ratio_extHyperlinks = st.number_input('ratio_extHyperlinks')
ratio_nullHyperlinks = st.number_input('ratio_nullHyperlinks')
nb_extCSS = st.number_input('nb_extCSS')
ratio_intRedirection = st.number_input('ratio_intRedirection')
ratio_extRedirection = st.number_input('ratio_extRedirection')
ratio_intErrors = st.number_input('ratio_intErrors')
ratio_extErrors = st.number_input('ratio_extErrors')
login_form = st.number_input('login_form')
external_favicon = st.number_input('external_favicon')
links_in_tags = st.number_input('links_in_tags')
submit_email = st.number_input('submit_email')
ratio_intMedia = st.number_input('ratio_intMedia')
ratio_extMedia = st.number_input('ratio_extMedia')
sfh = st.number_input('sfh')
iframe = st.number_input('iframe')
popup_window = st.number_input('popup_window')
safe_anchor = st.number_input('safe_anchor')
onmouseover = st.number_input('onmouseover')
right_clic = st.number_input('right_clic')
empty_title = st.number_input('empty_title')
domain_in_title = st.number_input('domain_in_title')
domain_with_copyright = st.number_input('domain_with_copyright')
whois_registered_domain = st.number_input('whois_registered_domain')
domain_registration_length = st.number_input('domain_registration_length')
domain_age = st.number_input('domain_age')
web_traffic = st.number_input('web_traffic')
dns_record = st.number_input('dns_record')
google_index = st.number_input('google_index')
page_rank = st.number_input('page_rank')

input_data = np.array([[ length_url, length_hostname, ip, nb_dots, nb_hyphens,
       nb_at, nb_qm, nb_and, nb_or, nb_eq, nb_underscore,
       nb_tilde, nb_percent, nb_slash, nb_star, nb_colon, nb_comma,
       nb_semicolumn, nb_dollar, nb_space, nb_www, nb_com,
       nb_dslash, http_in_path, https_token, ratio_digits_url,
       ratio_digits_host, punycode, port, tld_in_path,
       tld_in_subdomain, abnormal_subdomain, nb_subdomains,
       prefix_suffix, random_domain, shortening_service,
       path_extension, nb_redirection, nb_external_redirection,
       length_words_raw, char_repeat, shortest_words_raw,
       shortest_word_host, shortest_word_path, longest_words_raw,
       longest_word_host, longest_word_path, avg_words_raw,
       avg_word_host, avg_word_path, phish_hints, domain_in_brand,
       brand_in_subdomain, brand_in_path, suspecious_tld,
       statistical_report, nb_hyperlinks, ratio_intHyperlinks,
       ratio_extHyperlinks, ratio_nullHyperlinks, nb_extCSS,
       ratio_intRedirection, ratio_extRedirection, ratio_intErrors,
       ratio_extErrors, login_form, external_favicon, links_in_tags,
       submit_email, ratio_intMedia, ratio_extMedia, sfh, iframe,
       popup_window, safe_anchor, onmouseover, right_clic,
       empty_title, domain_in_title, domain_with_copyright,
       whois_registered_domain, domain_registration_length, domain_age,
       web_traffic, dns_record, google_index, page_rank]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ Phishing")
    else:
        st.success("✅ Legitimate ")

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
