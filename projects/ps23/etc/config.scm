;; This is an operating system configuration template
;; for a "bare bones" setup, with no X11 display server.

(use-modules (gnu))
(use-service-modules networking ssh)
(use-package-modules screen ssh)

(operating-system
 (host-name "ps23")
 (timezone "America/Chicago")
 (locale "en_US.utf8")

 ;; Boot in "legacy" UEFI mode.
 (bootloader (bootloader-configuration
  (bootloader grub-efi-bootloader)
  ))

 ;; It's fitting to support the equally bare bones ‘-nographic’
 ;; QEMU option, which also nicely sidesteps forcing QWERTY.
 (kernel-arguments (list "console=ttyS0,115200"))
 (file-systems (append
                (list (file-system
                        (device (file-system-label "ps23-root"))
                        (mount-point "/")
                        (type "ext4"))
                      (file-system
                        (device (file-system-label "ESP"))
                        (mount-point "/boot/efi")
                        (type "fat32")))
                %base-file-systems))

 ;; This is where user accounts are specified.  The "root"
 ;; account is implicit, and is initially created with the
 ;; empty password.
 (users (cons (user-account
               (name "alice")
               (comment "Bob's sister")
               (group "users")

               ;; Adding the account to the "wheel" group
               ;; makes it a sudoer.  Adding it to "audio"
               ;; and "video" allows the user to play sound
               ;; and access the webcam.
               (supplementary-groups '("wheel"
                                       "audio" "video")))
              %base-user-accounts))

 ;; Globally-installed packages.
 (packages (cons screen %base-packages))

 ;; Add services to the baseline: a DHCP client and
 ;; an SSH server.
 (services (append (list (service dhcp-client-service-type)
                         (service openssh-service-type
                                  (openssh-configuration
                                   (openssh openssh-sans-x)
                                   (port-number 2222))))
                   %base-services)))
