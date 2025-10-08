resource "aws_instance" "myinstance1" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  subnet_id              = aws_subnet.mysubnet1.id
  vpc_security_group_ids = [aws_security_group.mysg.id]
  user_data              = file("${path.module}/instance1-setup.sh")

  tags = {
    Name        = "${var.project_name}-instance-1"
    Environment = var.environment
  }
}

resource "aws_instance" "myinstance2" {
  ami                    = var.ami_id
  instance_type          = var.instance_type
  subnet_id              = aws_subnet.mysubnet2.id
  vpc_security_group_ids = [aws_security_group.mysg.id]
  user_data              = file("${path.module}/instance2-setup.sh")

  tags = {
    Name        = "${var.project_name}-instance-2"
    Environment = var.environment
  }
}
