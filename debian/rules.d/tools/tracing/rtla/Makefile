include $(top_rulesdir)/Makefile.inc

MAKE_RTLA := +CFLAGS='$(CFLAGS) $(CPPFLAGS)' LDFLAGS='$(LDFLAGS)' $(MAKE) -C $(top_srcdir)/$(OUTDIR) O=$(CURDIR)
MAKE_RTLA += PKG_CONFIG='$(PKG_CONFIG)'
MAKE_RTLA += V=1

all:
	$(MAKE_RTLA)

install:
	$(MAKE_RTLA) install
ifneq (,$(filter nodoc,$(DEB_BUILD_PROFILES)))
	rm -rf $(DESTDIR)/usr/share/man
endif

clean:
	rm -rf *
