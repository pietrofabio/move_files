dst = '//db-rb-fs001/data_qlik_desktop/data_source_apps/block_conversion_analysis/block_activities/FUP_OPT' \
      '/fup_opt_activity.xml '

f = open(dst, 'r', encoding="utf-8", errors='ignore')
content = f.read()
f.close()
f = open(dst[0:], 'w', encoding="utf-8")
f.write(content)
f.close()
