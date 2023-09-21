module "morpheus_cluster" {
  source = "../../modules/morpheus-web-k8s-eks-aws"
  db_password_secret_manager_name = var.db_password_secret_manager_name
  vpc_cidr = var.vpc_cidr
  vpc_public_subnets = var.vpc_public_subnets
  vpc_private_subnets = var.vpc_private_subnets
  eks_managed_service_node_group_name = var.eks_managed_service_node_group_name
  self_managed_gpu_adv_iam_role_name = var.self_managed_gpu_adv_iam_role_name
  self_managed_web_node_group_name = var.self_managed_web_node_group_name
  self_managed_web_iam_role_name = var.self_managed_web_iam_role_name
  self_managed_gpu_nodes_instance_type = var.self_managed_gpu_nodes_instance_type
  self_managed_gpu_node_group_name = var.self_managed_gpu_node_group_name
  self_managed_gpu_iam_role_name = var.self_managed_gpu_iam_role_name
  self_managed_gpu_node_min_size = var.self_managed_gpu_node_min_size
  self_managed_gpu_node_max_size = var.self_managed_gpu_node_max_size
  self_managed_gpu_nodes_device_size = var.self_managed_gpu_nodes_device_size
  self_managed_gpu_adv_node_group_name = var.self_managed_gpu_adv_node_group_name
  eks_managed_services_iam_role_name = var.eks_managed_services_iam_role_name
  self_managed_gpu_adv_nodes_instance_type = var.self_managed_gpu_adv_nodes_instance_type
  self_managed_gpu_adv_node_min_size = var.self_managed_gpu_adv_node_min_size
  self_managed_gpu_adv_node_max_size = var.self_managed_gpu_adv_node_max_size
  self_managed_gpu_adv_nodes_device_size = var.self_managed_gpu_adv_nodes_device_size
  self_managed_gpu_adv_node_desired_size = var.self_managed_gpu_adv_node_desired_size
  self_managed_head_node_min_size = var.self_managed_head_node_min_size
  self_managed_head_node_max_size = var.self_managed_head_node_max_size
  self_managed_head_node_desired_size = var.self_managed_head_node_desired_size
  self_managed_head_nodes_instance_type = var.self_managed_head_nodes_instance_type
  self_managed_head_iam_role_name = var.self_managed_head_iam_role_name
  scale_up_queue_threshold = var.scale_up_queue_threshold
  scale_up_period = var.scale_up_period
  scale_up_evaluation_period = var.scale_up_evaluation_period
  scale_up_scaling_adjustment = var.scale_up_scaling_adjustment
  scale_down_queue_threshold = var.scale_down_queue_threshold
  scale_down_period = var.scale_down_period
  scale_down_evaluation_period = var.scale_down_evaluation_period
  scale_down_scaling_adjustment = var.scale_down_scaling_adjustment
  scale_up_adv_queue_threshold = var.scale_up_adv_queue_threshold
  scale_up_adv_period = var.scale_up_period
  scale_up_adv_evaluation_period = var.scale_up_adv_evaluation_period
  scale_up_adv_scaling_adjustment = var.scale_up_adv_scaling_adjustment
  scale_down_adv_queue_threshold = var.scale_down_adv_queue_threshold
  scale_down_adv_period = var.scale_down_adv_period
  scale_down_adv_evaluation_period = var.scale_down_adv_evaluation_period
  scale_down_adv_scaling_adjustment = var.scale_down_adv_scaling_adjustment
  api_hostname = var.api_hostname
  client_hostname = var.client_hostname
  create_aws_auth_configmap = var.create_aws_auth_configmap
  manage_aws_auth_configmap = var.manage_aws_auth_configmap
  env = var.env
}
