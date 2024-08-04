;; This is an operating system configuration template
;; for a "bare bones" setup, with no X11 display server.

(use-modules (gnu))
(use-service-modules networking ssh)
(use-package-modules screen ssh)

(operating-system
  (locale "en_US.utf8")
  (timezone "America/Chicago")
  (host-name "ps23")

  ;; This is where user accounts are specified.  The "root"
  ;; account is implicit, and is initially created with the
  ;; empty password.
  (users (cons* (user-account
                  (name "dckc")
                  (comment "madmode.com")
                  (group "users")

                  ;; Adding the account to the "wheel" group
                  ;; makes it a sudoer.  Adding it to "audio"
                  ;; and "video" allows the user to play sound
                  ;; and access the webcam.
                  (supplementary-groups '("wheel" "netdev" "audio" "video")))
                %base-user-accounts))

  ;; Globally-installed packages.
  (packages (cons screen %base-packages))

  ;; Add services to the baseline: a DHCP client and
  ;; an SSH server.
  (services
   (append (list (service dhcp-client-service-type)
                 (service openssh-service-type
                          (openssh-configuration (openssh openssh-sans-x)
                                                 (authorized-keys `(("dckc" ,(local-file
                                                                              "../dckc.keys"))))
                                                 (port-number 2222))))
           %base-services))

  ;; Boot in UEFI mode.
  (bootloader (bootloader-configuration
                (bootloader grub-efi-bootloader)
                (targets (list "/boot/efi"))))

  ;; It's fitting to support the equally bare bones ‘-nographic’
  ;; QEMU option, which also nicely sidesteps forcing QWERTY.
  (kernel-arguments (list "console=ttyS0,115200"))
  (file-systems (cons* (file-system
                         (mount-point "/boot/efi")
                         (device (file-system-label "ESP"))
                         (type "vfat"))
                       (file-system
                         (mount-point "/")
                         (device (file-system-label "ps23-root"))
                         (type "ext4")) %base-file-systems)))
