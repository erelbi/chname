all: install

install:
	mkdir -p $(DESTDIR)/usr/share/chname
	@cp -rf src $(DESTDIR)/usr/share/chname/
	@cp -rf icons $(DESTDIR)/usr/share/chname/

	mkdir -p $(DESTDIR)/usr/share/applications
	@cp -rf Chname.desktop $(DESTDIR)/usr/share/applications/

	
	mkdir -p $(DESTDIR)/usr/share/polkit-1/actions
	@cp  config/tr.org.pardus.pkexec.pardus-hostname-change.policy /usr/share/polkit-1/actions/



uninstall:
	@rm -rf /usr/share/chname
	@rm -rf /usr/share/applications/Chname.desktop
.PHONY: install uninstall
