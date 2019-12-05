DESC_STACK_GUARD = "Stack Protectors (via -fstack-protector-all) are one of the many countermeasures to the stack buffer overflows security vulnerabilities."
SVRT_STACK_GUARD = 8.1

DESC_OBJC_ARC = "Objective-C automatic reference counting (via -fobjc-arc) helps to prevent use-after-free and use-after-release bugs."
SVRT_OBJC_ARC = 6.5

DESC_PIE = "Position independent executable (via -pie) makes harder for the attacker to find known code locations and exploit a vulnerability."
SVRT_PIE = 4

def run_tests(ipa, r2, u, r2h):
	u.test(ipa, r2h.has_import(r2, ["__stack_chk_guard", "_stack_chk_guard", "stack_chk_guard"]), "Stack smashing protection (-fstack-protector-all)", DESC_STACK_GUARD, SVRT_STACK_GUARD)
	u.test(ipa, r2h.has_import(r2, ["objc_autorelease"]), "Objective-C automatic reference counting (-fobjc-arc)", DESC_OBJC_ARC, SVRT_OBJC_ARC)
	u.test(ipa, r2h.has_info(r2, "pic"), "Full ASLR (-pie)", DESC_PIE, SVRT_PIE)

def name_test():
	return "Detection Compiler flags"